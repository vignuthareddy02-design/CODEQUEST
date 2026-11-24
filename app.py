from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from python_course import MODULES, REGIONS, PROJECTS, DAILY_CHALLENGES
from career_courses import COURSES

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "codequest.db"

app = Flask(__name__)
app.secret_key = "CHANGE-THIS-TO-A-LONG-RANDOM-SECRET-BEFORE-PUBLISHING"

COURSE_WORLDS = [
    {
        "id": 1, "name": "Beginner Village", "subtitle": "The first spark",
        "skill": "Python introduction and print()", "crystal": "First Crystal",
        "story": "The village communication bell has gone silent. Wizard Eldrin believes a simple message can awaken it. Your first task is to speak to the kingdom through Python.",
        "lessons": [
            {
                "id": 1, "title": "Your first Python spell", "topic": "print()",
                "story": "Eldrin hands you a glowing scroll. 'A computer follows instructions. Let's make it speak!'",
                "theory": "Programming means writing instructions that a computer can follow. Python is a programming language. The print() command displays information on the screen.",
                "example": 'print("Hello, Codoria!")\nprint("The adventure begins!")',
                "task": "Write a program that displays your name and the words: I will save Codoria!",
                "quiz": {"question": "Which Python command displays text on the screen?", "options": ["show()", "print()", "displayText()", "writeLine()"], "answer": 1, "explain": "print() displays text or values in Python."}
            }
        ]
    },
    {
        "id": 2, "name": "Crystal Forest", "subtitle": "Collect information",
        "skill": "Variables and data types", "crystal": "Memory Crystal",
        "story": "The forest remembers every traveler, but its memory crystal is broken. Store names, numbers and useful information to restore it.",
        "lessons": [
            {"id": 2, "title": "The memory boxes", "topic": "Variables",
             "story": "A forest keeper gives you three magical boxes. Each box can hold a piece of information.",
             "theory": "A variable is a named place where a program stores a value. Think of it like a labelled box. Use = to put a value inside it.",
             "example": 'hero = "Arin"\nlevel = 1\nprint(hero)\nprint(level)',
             "task": "Create a variable called favourite_food and store the name of a food in it. Print the variable.",
             "quiz": {"question": "What is a variable?", "options": ["A named place to store a value", "A type of computer", "A Python error", "A website"], "answer": 0, "explain": "A variable stores a value under a name."}}
        ]
    },
    {
        "id": 3, "name": "Castle of Decisions", "subtitle": "Choose your path",
        "skill": "Operators and if/else", "crystal": "Choice Crystal",
        "story": "The castle gate opens only for a traveler whose answer is correct. Teach the gate to make decisions.",
        "lessons": [
            {"id": 3, "title": "The gatekeeper's choice", "topic": "if and else",
             "story": "The gatekeeper asks whether your energy is high enough to enter. Your code must choose what happens.",
             "theory": "Programs can make decisions. An if statement runs code when a condition is true. else runs when it is false. Python uses indentation to show which lines belong together.",
             "example": 'energy = 8\nif energy >= 5:\n    print("The gate opens!")\nelse:\n    print("Find more energy.")',
             "task": "Create a variable called coins. If coins is 10 or more, print You can buy a key! Otherwise print Keep collecting coins.",
             "quiz": {"question": "When does the else block run?", "options": ["Always first", "When the if condition is false", "Only when Python closes", "Never"], "answer": 1, "explain": "else provides the alternative when the if condition is false."}}
        ]
    },
    {
        "id": 4, "name": "Looping Mountains", "subtitle": "Repeat the magic",
        "skill": "for and while loops", "crystal": "Motion Crystal",
        "story": "The mountain lifts work only when the same action is repeated. Repair the machines by teaching them loops.",
        "lessons": [
            {"id": 4, "title": "The repeating bridge", "topic": "for loops",
             "story": "A bridge builder needs you to place five stones. Instead of writing the same instruction five times, teach the machine to repeat.",
             "theory": "A loop repeats a block of code. A for loop is useful when you want to go through a sequence or repeat something a known number of times.",
             "example": 'for stone in range(5):\n    print("Place a stone")',
             "task": "Use a for loop and range(3) to print Ready! three times.",
             "quiz": {"question": "What is a loop used for?", "options": ["Repeating instructions", "Deleting Python", "Changing the keyboard", "Creating a folder"], "answer": 0, "explain": "Loops repeat instructions without copying the same code many times."}}
        ]
    },
    {
        "id": 5, "name": "Wizard's Academy", "subtitle": "Create reusable spells",
        "skill": "Functions", "crystal": "Spell Crystal",
        "story": "The wizard knows hundreds of spells. He stores each spell under a name so he can use it whenever needed.",
        "lessons": [
            {"id": 5, "title": "Create your first spell", "topic": "Functions",
             "story": "Eldrin teaches you to package instructions into a reusable spell called a function.",
             "theory": "A function is a reusable block of code. Define it with def, give it a name, and call it whenever you need it.",
             "example": 'def greet(hero):\n    print("Welcome, " + hero)\n\ngreet("Arin")',
             "task": "Create a function called say_hello that prints Hello, adventurer! Then call the function.",
             "quiz": {"question": "Which keyword defines a function in Python?", "options": ["function", "make", "def", "repeat"], "answer": 2, "explain": "Python uses the def keyword to define a function."}}
        ]
    },
    {
        "id": 6, "name": "Inventory Kingdom", "subtitle": "Organize your items",
        "skill": "Lists, tuples, sets and dictionaries", "crystal": "Inventory Crystal",
        "story": "The kingdom's inventory is scattered. Organize potions, keys and maps so every explorer can find what they need.",
        "lessons": [
            {"id": 6, "title": "The explorer's backpack", "topic": "Lists",
             "story": "You receive a backpack that can hold many items. Add, remove and inspect what is inside.",
             "theory": "A list stores multiple values in one variable. Lists keep their order and can be changed after creation.",
             "example": 'backpack = ["map", "key", "potion"]\nprint(backpack)\nbackpack.append("compass")\nprint(backpack)',
             "task": "Create a list with three adventure items. Add a fourth item using append() and print the list.",
             "quiz": {"question": "Which method adds an item to the end of a list?", "options": ["push()", "append()", "insertEnd()", "addLast()"], "answer": 1, "explain": "append() adds an item to the end of a Python list."}}
        ]
    },
    {
        "id": 7, "name": "Shadow Dungeon", "subtitle": "Solve hidden mysteries",
        "skill": "Strings, exceptions and files", "crystal": "Knowledge Crystal",
        "story": "The dungeon contains old messages and locked records. Read clues safely and handle unexpected problems.",
        "lessons": [
            {"id": 7, "title": "The hidden message", "topic": "Strings",
             "story": "A mysterious message is written on the dungeon wall. Learn how text is stored and explored.",
             "theory": "A string is text surrounded by quotes. You can join strings, find their length and access individual characters.",
             "example": 'clue = "CODEQUEST"\nprint(len(clue))\nprint(clue[0])',
             "task": "Store the word DRAGON in a variable and print its length.",
             "quiz": {"question": "Which value is a string?", "options": ["42", "3.14", '"Codoria"', "True"], "answer": 2, "explain": "Text inside quotes is a string."}}
        ]
    },
    {
        "id": 8, "name": "Dragon's Fortress", "subtitle": "Master object-oriented magic",
        "skill": "Classes, objects and inheritance", "crystal": "Power Crystal",
        "story": "A dragon guards the next crystal. Build your own reusable character blueprint and understand how objects behave.",
        "lessons": [
            {"id": 8, "title": "Build a hero blueprint", "topic": "Classes and objects",
             "story": "The royal inventor gives you a blueprint for creating heroes with names and powers.",
             "theory": "A class is a blueprint. An object is something created from that blueprint. Objects can store data in attributes and perform actions using methods.",
             "example": 'class Hero:\n    def __init__(self, name):\n        self.name = name\n\n    def introduce(self):\n        print("I am " + self.name)\n\nhero = Hero("Arin")\nhero.introduce()',
             "task": "Create a class called Pet with a name attribute and a method that prints the pet's name.",
             "quiz": {"question": "What is a class?", "options": ["A blueprint for objects", "A loop", "A number", "A Python package only"], "answer": 0, "explain": "A class defines the structure and behavior of objects."}}
        ]
    },
    {
        "id": 9, "name": "Crystal Core", "subtitle": "Become the kingdom's creator",
        "skill": "Projects and combining concepts", "crystal": "The Code Crystal",
        "story": "All the crystal fragments are ready. Combine your skills to restore Codoria's central system and become its guardian developer.",
        "lessons": [
            {"id": 9, "title": "Restore the Code Crystal", "topic": "Final Python project",
             "story": "The final console is waiting. Build a small adventure program using variables, decisions, loops and functions.",
             "theory": "Real programs combine many concepts. Plan the steps, break the work into functions, test small pieces and improve your solution.",
             "example": 'def welcome(name):\n    print("Welcome to Codoria, " + name)\n\nhero = input("Enter your name: ")\nwelcome(hero)',
             "task": "Build a mini text adventure. Ask the player for a name, welcome them, and use an if/else choice to decide which path they take.",
             "quiz": {"question": "What is a good way to build a larger program?", "options": ["Put everything in one confusing line", "Break it into smaller parts and test them", "Never test it", "Avoid meaningful names"], "answer": 1, "explain": "Breaking a program into smaller parts makes it easier to build and debug."}}
        ]
    }
]

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            hero_name TEXT DEFAULT '',
            xp INTEGER DEFAULT 0,
            completed TEXT DEFAULT ''
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS python_progress (
            user_id INTEGER NOT NULL, module_id INTEGER NOT NULL,
            lesson_complete INTEGER DEFAULT 0, quiz_best REAL DEFAULT 0,
            quiz_passed INTEGER DEFAULT 0, exam_best REAL DEFAULT 0,
            exam_passed INTEGER DEFAULT 0, practice_solved INTEGER DEFAULT 0,
            updated_at TEXT, PRIMARY KEY(user_id, module_id),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS python_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL,
            module_id INTEGER NOT NULL, kind TEXT NOT NULL, score REAL NOT NULL,
            total INTEGER NOT NULL, passed INTEGER NOT NULL, answers TEXT,
            created_at TEXT NOT NULL, FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS python_practice_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL,
            module_id INTEGER NOT NULL, practice_id TEXT NOT NULL,
            submitted TEXT DEFAULT '', completed INTEGER DEFAULT 0,
            created_at TEXT NOT NULL, UNIQUE(user_id, practice_id)
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS python_project_progress (
            user_id INTEGER NOT NULL, project_id TEXT NOT NULL, completed INTEGER DEFAULT 0,
            completed_at TEXT, PRIMARY KEY(user_id, project_id)
        )""")
        conn.execute("""CREATE TABLE IF NOT EXISTS career_topic_progress (
            user_id INTEGER NOT NULL, course_slug TEXT NOT NULL, topic_key TEXT NOT NULL,
            completed_at TEXT NOT NULL, PRIMARY KEY(user_id, course_slug, topic_key),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper

def current_user():
    if "user_id" not in session:
        return None
    with db() as conn:
        return conn.execute("SELECT * FROM users WHERE id=?", (session["user_id"],)).fetchone()

@app.route("/")
def home():
    return render_template("index.html", user=current_user())

@app.route("/languages")
def languages():
    catalog = [
        {"slug": "java", "name": "Java Empire", "icon": "☕", "class": "java-card", "description": "Core Java, OOP, collections, Spring Boot, testing and projects.", "topics": "12 modules · Core Java · Spring Boot"},
        {"slug": "c", "name": "C Kingdom", "icon": "⚙️", "class": "c-card", "description": "Build strong foundations with logic, memory, pointers and data structures.", "topics": "Basics · Pointers · Data structures"},
        {"slug": "cpp", "name": "C++ Realm", "icon": "💠", "class": "cpp-card", "description": "Explore object-oriented programming, STL and problem solving.", "topics": "OOP · STL · Algorithms"},
        {"slug": "javascript", "name": "JavaScript Islands", "icon": "🌐", "class": "web-card", "description": "Create interactive websites and learn modern JavaScript.", "topics": "JavaScript · DOM · Async"},
        {"slug": "sql", "name": "SQL Underworld", "icon": "🗄️", "class": "sql-card", "description": "Master queries, joins, database design, optimization and data projects.", "topics": "14 modules · Queries · Joins"},
        {"slug": "devops", "name": "DevOps Universe", "icon": "🚀", "class": "devops-card", "description": "Travel through Linux, Git, Jenkins, Docker, Kubernetes, AWS and CI/CD.", "topics": "14 modules · Linux · Docker · AWS"},
        {"slug": "html-css", "name": "HTML & CSS Enchanted Isles", "icon": "🎨", "class": "design-card", "description": "Turn ideas into beautiful responsive web pages.", "topics": "HTML · CSS · Responsive design"},
    ]
    return render_template("languages.html", user=current_user(), languages=catalog)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if not username or not email or len(password) < 8:
            flash("Enter your name, a valid email and a password with at least 8 characters.", "error")
            return redirect(url_for("register"))
        try:
            with db() as conn:
                cur = conn.execute("INSERT INTO users(username,email,password_hash) VALUES(?,?,?)",
                                   (username, email, generate_password_hash(password)))
                session["user_id"] = cur.lastrowid
            return redirect(url_for("character"))
        except sqlite3.IntegrityError:
            flash("That email already has an account. Please log in.", "error")
    return render_template("auth.html", mode="register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        with db() as conn:
            user = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            return redirect(url_for("adventure"))
        flash("Email or password is incorrect.", "error")
    return render_template("auth.html", mode="login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/character", methods=["GET", "POST"])
@login_required
def character():
    user = current_user()
    if request.method == "POST":
        hero_name = request.form.get("hero_name", "").strip()[:24]
        if hero_name:
            with db() as conn:
                conn.execute("UPDATE users SET hero_name=? WHERE id=?", (hero_name, user["id"]))
            return redirect(url_for("adventure"))
        flash("Choose a hero name to continue.", "error")
    return render_template("character.html", user=user)

@app.route("/adventure")
@login_required
def adventure():
    user = current_user()
    completed = [int(x) for x in user["completed"].split(",") if x.strip().isdigit()]
    worlds = []
    for world in COURSE_WORLDS:
        item = dict(world)
        item["done"] = world["id"] in completed
        item["unlocked"] = world["id"] == 1 or (world["id"] - 1) in completed
        worlds.append(item)
    return render_template("adventure.html", user=user, worlds=worlds, completed=len(completed))

@app.route("/lesson/<int:world_id>")
@login_required
def lesson(world_id):
    if world_id < 1 or world_id > len(COURSE_WORLDS):
        return redirect(url_for("adventure"))
    user = current_user()
    completed = [int(x) for x in user["completed"].split(",") if x.strip().isdigit()]
    if world_id > 1 and world_id - 1 not in completed:
        flash("Complete the previous mission to unlock this world.", "error")
        return redirect(url_for("adventure"))
    world = COURSE_WORLDS[world_id - 1]
    return render_template("lesson.html", user=user, world=world, lesson=world["lessons"][0])

@app.route("/complete/<int:world_id>", methods=["POST"])
@login_required
def complete(world_id):
    if world_id < 1 or world_id > len(COURSE_WORLDS):
        return jsonify({"ok": False, "message": "Unknown mission"}), 400
    with db() as conn:
        user = conn.execute("SELECT * FROM users WHERE id=?", (session["user_id"],)).fetchone()
        completed = [int(x) for x in user["completed"].split(",") if x.strip().isdigit()]
        if world_id not in completed:
            completed.append(world_id)
            conn.execute("UPDATE users SET completed=?, xp=xp+100 WHERE id=?",
                         (",".join(map(str, completed)), session["user_id"]))
        updated = conn.execute("SELECT xp FROM users WHERE id=?", (session["user_id"],)).fetchone()
    return jsonify({"ok": True, "xp": updated["xp"], "completed": len(completed)})


def python_progress_for(user_id):
    with db() as conn:
        rows = conn.execute("SELECT * FROM python_progress WHERE user_id=?", (user_id,)).fetchall()
    return {row['module_id']: dict(row) for row in rows}

def python_module_unlocked(module_id, progress):
    if module_id == 1:
        return True
    previous = progress.get(module_id - 1)
    return bool(previous and previous['exam_passed'])

def python_exam_questions(module):
    questions = [dict(q) for q in module['quiz']]
    for i, example in enumerate(module['examples']):
        questions.append({'type':'output','question':f"Which concept is demonstrated by the example '{example['title']}'?",'options':[example['explanation'], 'A CSS layout rule', 'A database server setting', 'A hardware instruction'],'answer':0,'explanation':example['explanation']})
        questions.append({'type':'debug','question':f"Find the error after adapting '{example['title']}'.",'code':example['code'] + "\nprint(missing_variable)",'options':['The final line references missing_variable before it is defined','Python does not allow print statements','The code must use a class','All variable names must be uppercase'],'answer':0,'explanation':'The final print refers to a name that has not been assigned. Define it first or print an existing name.'})
        task = module['exercises'][i]
        questions.append({'type':'coding','question':f"Practical coding task: {task}",'options':['Break it into small steps, implement the required logic, and test edge cases','Print a fixed answer without using the input','Ignore invalid data and boundary cases','Copy an unrelated example without adapting it'],'answer':0,'explanation':'A sound solution follows the requirement, uses appropriate concepts and verifies edge cases.'})
    for i, task in enumerate(module['exercises'][:3]):
        questions.append({'type':'coding','question':f"Practical problem {i+1}: {task}",'options':['Plan the steps, write a reusable solution and test normal plus edge cases','Hard-code the expected output','Skip input validation and testing','Use unrelated code without understanding it'],'answer':0,'explanation':'A complete programming solution must satisfy the requirement and be tested with representative edge cases.'})
    return questions[:30]

@app.route('/python')
@login_required
def python_course():
    user = current_user()
    progress = python_progress_for(user['id'])
    modules = []
    passed = sum(1 for p in progress.values() if p['exam_passed'])
    with db() as conn:
        practice_count = conn.execute('SELECT COUNT(*) FROM python_practice_attempts WHERE user_id=? AND completed=1', (user['id'],)).fetchone()[0]
        project_rows = conn.execute('SELECT project_id FROM python_project_progress WHERE user_id=? AND completed=1', (user['id'],)).fetchall()
        project_ids = {row['project_id'] for row in project_rows}
    lesson_count = sum(1 for p in progress.values() if p['lesson_complete'])
    quiz_count = sum(1 for p in progress.values() if p['quiz_passed'])
    exam_count = passed
    total_units = len(MODULES) * 3 + len(MODULES) * 25 + len(PROJECTS)
    done_units = lesson_count + quiz_count + exam_count + practice_count + len(project_ids)
    for module in MODULES:
        p = progress.get(module['id'], {})
        unlocked = python_module_unlocked(module['id'], progress)
        modules.append({'id':module['id'], 'title':module['title'], 'intro':module['intro'],
                        'region': next((r['name'] for r in REGIONS if r['range'][0] <= module['id'] <= r['range'][1]), 'Python Kingdom'),
                        'unlocked':unlocked, 'lesson_complete':bool(p.get('lesson_complete',0)),
                        'quiz_passed':bool(p.get('quiz_passed',0)), 'exam_passed':bool(p.get('exam_passed',0)),
                        'exam_best':p.get('exam_best',0), 'quiz_best':p.get('quiz_best',0)})
    percent = round(done_units / total_units * 100)
    return render_template('python_course.html', user=user, modules=modules, regions=REGIONS,
                           passed=passed, percent=percent, progress=progress,
                           lesson_count=lesson_count, quiz_count=quiz_count, practice_count=practice_count,
                           project_count=len(project_ids), project_total=len(PROJECTS))

@app.route('/python/module/<int:module_id>')
@login_required
def python_module(module_id):
    if not 1 <= module_id <= len(MODULES):
        return redirect(url_for('python_course'))
    user = current_user()
    progress = python_progress_for(user['id'])
    if not python_module_unlocked(module_id, progress):
        flash('Pass the previous module examination with at least 70% to unlock this lesson.', 'error')
        return redirect(url_for('python_course'))
    module = MODULES[module_id - 1]
    p = progress.get(module_id, {})
    with db() as conn:
        attempts = conn.execute("SELECT kind, score, total, passed, created_at FROM python_attempts WHERE user_id=? AND module_id=? ORDER BY id DESC LIMIT 8", (user['id'], module_id)).fetchall()
    return render_template('python_module.html', user=user, module=module, progress=p, attempts=attempts)

@app.route('/python/complete-lesson/<int:module_id>', methods=['POST'])
@login_required
def python_complete_lesson(module_id):
    if not 1 <= module_id <= len(MODULES):
        return jsonify({'ok':False, 'message':'Unknown module'}), 404
    progress = python_progress_for(session['user_id'])
    if not python_module_unlocked(module_id, progress):
        return jsonify({'ok':False, 'message':'Module is locked'}), 403
    with db() as conn:
        conn.execute("INSERT INTO python_progress(user_id,module_id,lesson_complete,updated_at) VALUES(?,?,1,?) ON CONFLICT(user_id,module_id) DO UPDATE SET lesson_complete=1, updated_at=excluded.updated_at", (session['user_id'], module_id, datetime.now(timezone.utc).isoformat()))
    return jsonify({'ok':True, 'message':'Lesson marked complete. Take the topic quiz next.'})

@app.route('/python/quiz/<int:module_id>')
@login_required
def python_quiz(module_id):
    if not 1 <= module_id <= len(MODULES): return redirect(url_for('python_course'))
    progress = python_progress_for(session['user_id'])
    if not python_module_unlocked(module_id, progress): return redirect(url_for('python_course'))
    module = MODULES[module_id-1]
    questions = [dict(q, qid=i) for i,q in enumerate(module['quiz'])]
    random.shuffle(questions)
    return render_template('python_assessment.html', user=current_user(), module=module, questions=questions, kind='quiz', duration=15, pass_mark=70)

@app.route('/python/exam/<int:module_id>')
@login_required
def python_exam(module_id):
    if not 1 <= module_id <= len(MODULES): return redirect(url_for('python_course'))
    progress = python_progress_for(session['user_id'])
    p = progress.get(module_id, {})
    if not p.get('lesson_complete') or not p.get('quiz_passed'):
        flash('Complete the lesson and pass its topic quiz before starting the module examination.', 'error')
        return redirect(url_for('python_module', module_id=module_id))
    module = MODULES[module_id-1]
    questions = python_exam_questions(module)
    indexed = list(enumerate(questions))
    random.shuffle(indexed)
    questions = [dict(q, qid=i) for i,q in indexed]
    return render_template('python_assessment.html', user=current_user(), module=module, questions=questions, kind='exam', duration=60, pass_mark=70)

@app.route('/python/weekly-test/<int:week>')
@login_required
def python_weekly_test(week):
    if not 1 <= week <= 6: return redirect(url_for('python_revision'))
    start = (week - 1) * 7
    end = min(start + 7, len(MODULES))
    questions = []
    source_pairs = []
    for module_index in range(start, end):
        for question_index in (0, 1):
            q = dict(MODULES[module_index]['quiz'][question_index], qid=len(questions))
            questions.append(q)
            source_pairs.append([module_index + 1, question_index])
    indexed = list(zip(questions, source_pairs))
    random.shuffle(indexed)
    questions = []
    source_pairs = []
    for q, pair in indexed:
        q['qid'] = len(questions)
        questions.append(q)
        source_pairs.append(pair)
    session['python_weekly_pairs'] = source_pairs
    display_module = {'id':week, 'title':f'Weekly Python Checkpoint {week}'}
    return render_template('python_assessment.html', user=current_user(), module=display_module,
                           questions=questions, kind='weekly', duration=25, pass_mark=70)

@app.route('/python/mock-exam')
@login_required
def python_mock_exam():
    questions = []
    for module in MODULES:
        for question in module['quiz'][:1]:
            questions.append(dict(question, qid=len(questions), source_module=module['id']))
    random.shuffle(questions)
    # Store question order and reset IDs to match the displayed paper.
    for index, question in enumerate(questions): question['qid'] = index
    session['python_mock_question_ids'] = [q['source_module'] for q in questions]
    display_module = {'id':0, 'title':'Full Python Mock Examination'}
    return render_template('python_assessment.html', user=current_user(), module=display_module,
                           questions=questions, kind='mock', duration=60, pass_mark=70)

@app.route('/python/submit/<kind>/<int:module_id>', methods=['POST'])
@login_required
def python_submit_assessment(kind, module_id):
    if kind not in ('quiz','exam','mock','weekly') or (kind in ('quiz','exam') and not 1 <= module_id <= len(MODULES)) or (kind == 'mock' and module_id != 0) or (kind == 'weekly' and not 1 <= module_id <= 6):
        return jsonify({'ok':False,'message':'Invalid assessment'}), 400
    progress = python_progress_for(session['user_id'])
    if kind in ('quiz','exam') and not python_module_unlocked(module_id, progress): return jsonify({'ok':False,'message':'Module locked'}), 403
    module = MODULES[module_id-1] if kind in ('quiz','exam') else None
    if kind == 'exam' and not (progress.get(module_id,{}).get('lesson_complete') and progress.get(module_id,{}).get('quiz_passed')):
        return jsonify({'ok':False,'message':'Complete the lesson and pass the quiz first'}), 403
    if kind == 'quiz':
        questions = [dict(q, qid=i) for i,q in enumerate(module['quiz'])]
    elif kind == 'exam':
        questions = [dict(q, qid=i) for i,q in enumerate(python_exam_questions(module))]
    elif kind == 'mock':
        source_ids = session.get('python_mock_question_ids', [])
        questions = [dict(MODULES[mid-1]['quiz'][0], qid=i) for i,mid in enumerate(source_ids)]
        if len(questions) != 40: return jsonify({'ok':False,'message':'Mock exam expired. Start it again.'}), 400
    else:
        pairs = session.get('python_weekly_pairs', [])
        questions = [dict(MODULES[mid-1]['quiz'][qid], qid=i) for i,(mid,qid) in enumerate(pairs)]
        if not questions: return jsonify({'ok':False,'message':'Weekly test expired. Start it again.'}), 400
    answers = request.get_json(silent=True) or {}
    correct = 0
    analysis = []
    for index, question in enumerate(questions):
        selected = answers.get(str(question.get('qid', index)))
        try: selected = int(selected)
        except (TypeError, ValueError): selected = -1
        is_correct = selected == question['answer']
        correct += int(is_correct)
        analysis.append({'question':question['question'], 'selected':selected,
                         'correct_answer':question['answer'], 'options':question['options'],
                         'type':question.get('type','knowledge'), 'code':question.get('code'), 'is_correct':is_correct,
                         'explanation':question['explanation']})
    score = round(correct / len(questions) * 100, 1)
    passed = score >= 70
    type_summary = {}
    for item in analysis:
        group = type_summary.setdefault(item['type'], {'correct':0,'total':0})
        group['total'] += 1
        group['correct'] += int(item['is_correct'])
    for group in type_summary.values():
        group['score'] = round(group['correct'] / group['total'] * 100, 1)
    now = datetime.now(timezone.utc).isoformat()
    with db() as conn:
        conn.execute("INSERT INTO python_attempts(user_id,module_id,kind,score,total,passed,answers,created_at) VALUES(?,?,?,?,?,?,?,?)",
                     (session['user_id'], -module_id if kind == 'weekly' else module_id, kind, score, len(questions), int(passed), json.dumps(analysis), now))
        if kind == 'quiz':
            conn.execute("INSERT INTO python_progress(user_id,module_id,quiz_best,quiz_passed,updated_at) VALUES(?,?,?,?,?) ON CONFLICT(user_id,module_id) DO UPDATE SET quiz_best=MAX(quiz_best,excluded.quiz_best), quiz_passed=MAX(quiz_passed,excluded.quiz_passed), updated_at=excluded.updated_at",
                         (session['user_id'], module_id, score, int(passed), now))
        elif kind == 'exam':
            previous = conn.execute('SELECT exam_passed FROM python_progress WHERE user_id=? AND module_id=?', (session['user_id'], module_id)).fetchone()
            first_pass = passed and not (previous and previous['exam_passed'])
            conn.execute("INSERT INTO python_progress(user_id,module_id,exam_best,exam_passed,updated_at) VALUES(?,?,?,?,?) ON CONFLICT(user_id,module_id) DO UPDATE SET exam_best=MAX(exam_best,excluded.exam_best), exam_passed=MAX(exam_passed,excluded.exam_passed), updated_at=excluded.updated_at",
                         (session['user_id'], module_id, score, int(passed), now))
            if first_pass:
                conn.execute("UPDATE users SET xp=xp+100 WHERE id=?", (session['user_id'],))
    if kind == 'exam' and passed and module_id < len(MODULES):
        next_url = url_for('python_module', module_id=module_id+1)
    elif kind == 'exam' and not passed:
        next_url = url_for('python_exam', module_id=module_id)
    elif kind == 'quiz' and passed:
        next_url = url_for('python_module', module_id=module_id)
    elif kind == 'quiz':
        next_url = url_for('python_quiz', module_id=module_id)
    else:
        next_url = url_for('python_revision')
    return jsonify({'ok':True, 'score':score, 'correct':correct, 'total':len(questions), 'passed':passed,
                    'pass_mark':70, 'analysis':analysis, 'type_summary':type_summary, 'next_url':next_url})

@app.route('/python/practice/<int:module_id>/<practice_id>', methods=['POST'])
@login_required
def python_practice_save(module_id, practice_id):
    if not 1 <= module_id <= len(MODULES): return jsonify({'ok':False}), 404
    progress = python_progress_for(session['user_id'])
    if not python_module_unlocked(module_id, progress): return jsonify({'ok':False,'message':'Module locked'}), 403
    module = MODULES[module_id-1]
    item = next((x for x in module['practice'] if x['id'] == practice_id), None)
    if not item: return jsonify({'ok':False}), 404
    payload = request.get_json(silent=True) or {}
    submitted = str(payload.get('answer',''))[:12000]
    if not submitted.strip(): return jsonify({'ok':False,'message':'Write an attempt before saving.'}), 400
    with db() as conn:
        conn.execute("INSERT INTO python_practice_attempts(user_id,module_id,practice_id,submitted,completed,created_at) VALUES(?,?,?,?,1,?) ON CONFLICT(user_id,practice_id) DO UPDATE SET submitted=excluded.submitted,completed=1,created_at=excluded.created_at",
                     (session['user_id'], module_id, practice_id, submitted, datetime.now(timezone.utc).isoformat()))
        solved = conn.execute('SELECT COUNT(*) FROM python_practice_attempts WHERE user_id=? AND module_id=? AND completed=1', (session['user_id'], module_id)).fetchone()[0]
        conn.execute("INSERT INTO python_progress(user_id,module_id,practice_solved,updated_at) VALUES(?,?,?,?) ON CONFLICT(user_id,module_id) DO UPDATE SET practice_solved=excluded.practice_solved, updated_at=excluded.updated_at",
                     (session['user_id'], module_id, solved, datetime.now(timezone.utc).isoformat()))
    return jsonify({'ok':True,'message':'Your practice attempt has been saved.'})

@app.route('/python/projects')
@login_required
def python_projects():
    with db() as conn:
        done = {row['project_id'] for row in conn.execute('SELECT project_id FROM python_project_progress WHERE user_id=? AND completed=1', (session['user_id'],)).fetchall()}
    projects = [dict(p, completed=p['id'] in done) for p in PROJECTS]
    return render_template('python_projects.html', user=current_user(), projects=projects, completed=len(done))

@app.route('/python/projects/<project_id>/complete', methods=['POST'])
@login_required
def python_project_complete(project_id):
    if not any(p['id'] == project_id for p in PROJECTS): return jsonify({'ok':False,'message':'Unknown project'}), 404
    with db() as conn:
        conn.execute("INSERT INTO python_project_progress(user_id,project_id,completed,completed_at) VALUES(?,?,1,?) ON CONFLICT(user_id,project_id) DO UPDATE SET completed=1,completed_at=excluded.completed_at",
                     (session['user_id'], project_id, datetime.now(timezone.utc).isoformat()))
    return jsonify({'ok':True,'message':'Project marked complete.'})

@app.route('/python/daily')
@login_required
def python_daily():
    today = datetime.now().date().isoformat()
    return render_template('python_daily.html', user=current_user(), challenges=DAILY_CHALLENGES, today=today)

@app.route('/python/revision')
@login_required
def python_revision():
    weeks = []
    for index, start in enumerate(range(0, len(MODULES), 7), 1):
        weeks.append({'week':index, 'modules':MODULES[start:start+7]})
    return render_template('python_revision.html', user=current_user(), modules=MODULES, weeks=weeks)


@app.route('/course/<slug>')
@login_required
def career_course(slug):
    course = COURSES.get(slug)
    if not course:
        return redirect(url_for('languages'))
    total_topics = sum(len(module['topics']) for module in course['modules'])
    with db() as conn:
        rows = conn.execute('SELECT topic_key FROM career_topic_progress WHERE user_id=? AND course_slug=?', (session['user_id'], slug)).fetchall()
    done = {row['topic_key'] for row in rows}
    completed = len(done)
    percent = round(completed / total_topics * 100) if total_topics else 0
    return render_template('career_courses.html', user=current_user(), course=course,
                           total_topics=total_topics, completed=completed, percent=percent, done=done)

@app.route('/course/<slug>/module/<int:module_id>/topic/<int:topic_no>/complete', methods=['POST'])
@login_required
def career_topic_complete(slug, module_id, topic_no):
    course = COURSES.get(slug)
    if not course or not 1 <= module_id <= len(course['modules']):
        return redirect(url_for('languages'))
    module = course['modules'][module_id - 1]
    if not 1 <= topic_no <= len(module['topics']):
        return redirect(url_for('career_course', slug=slug))
    topic_key = f'{module_id}:{topic_no}'
    with db() as conn:
        conn.execute('INSERT OR IGNORE INTO career_topic_progress(user_id,course_slug,topic_key,completed_at) VALUES(?,?,?,?)',
                     (session['user_id'], slug, topic_key, datetime.now(timezone.utc).isoformat()))
    flash('Topic progress saved. Keep going!', 'success')
    return redirect(url_for('career_course', slug=slug) + f'#module-{module_id}')

@app.route("/api/worlds")
@login_required
def api_worlds():
    return jsonify([{"id": w["id"], "name": w["name"], "skill": w["skill"]} for w in COURSE_WORLDS])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
