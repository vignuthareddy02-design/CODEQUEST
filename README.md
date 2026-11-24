# CODEQUEST – The Lost Kingdom

A Flask + SQLite learning game with a story-driven Python course. The original CODEQUEST look, login, adventure map, sound controls and browser Python playground are retained.

## Python learning path

The Python Kingdom contains **40 ordered modules**, from Python introduction and setup through syntax, collections, functions, OOP, advanced language features, data libraries, SQL, APIs, scraping, automation, Flask, Django, FastAPI, testing, Git, analytics, AI/ML, professional development, interview preparation and capstone work.

Each module includes:
- Beginner-friendly introduction, definition, purpose, real-life uses and prerequisites
- Detailed explanation, key concepts and syntax notes
- Five practical code examples with expected output/behavior and line walkthroughs
- Common mistakes, tips, interview questions, revision notes and a summary
- 25 exercises: five beginner, five intermediate, five advanced, five output-prediction and five debugging tasks
- A 12-question topic quiz with randomized display, automatic scoring, explanations, retry and saved attempts
- A 30-question module examination with a 60-minute timer and 70% pass requirement

The Python course dashboard groups the 40 modules into the existing fantasy regions. A module unlocks after the previous module examination is passed. Passing an exam for the first time awards 100 XP. Progress is stored in SQLite.

Additional learning areas:
- Daily easy, medium and hard coding challenges
- 20 guided projects across beginner, intermediate and advanced levels
- Revision centre with searchable notes, syntax summaries, flashcards, weekly checkpoints and a 40-question full-course mock exam
- Saved practice attempts, project completion, quiz scores, exam scores and overall course progress

## Run on Windows PowerShell

Open the **CODEQUEST** folder (the one containing `app.py`) in VS Code. In its terminal run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser. If PowerShell blocks activation, run this once in the current user scope:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## Course routes

- `/python` – 40-module Python roadmap
- `/python/module/1` – first topic lesson
- `/python/quiz/1` – topic quiz
- `/python/exam/1` – module examination (available after lesson completion and quiz pass)
- `/python/daily` – daily coding challenges
- `/python/projects` – project workshop
- `/python/revision` – revision centre
- `/python/mock-exam` – full-course mock examination

All learning routes require a signed-in account.

## Runtime notes

The in-browser editor uses Pyodide and needs an internet connection to load. It supports core Python well, but operating-system commands, Git, Django project management, database drivers and some scientific packages need a local Python environment and their stated dependencies. For those lessons, run the examples in your local virtual environment after installing the package named in the lesson. The course content calls out those setup requirements instead of pretending every external library is built into the browser runtime.

This project is a learning starter, not a production deployment. Before publishing it, set a strong secret key through environment configuration, enable HTTPS and secure session cookies, add CSRF protection to forms, configure production logging, and run a security review. Never commit real credentials or `.env` files.

## Java, DevOps and SQL course integration (Phase 1)

The Languages page now links signed-in learners to three additional course roadmaps:

- `/course/java` — 12 Java modules
- `/course/devops` — 15 DevOps modules
- `/course/sql` — 14 SQL modules

The roadmap data lives in `career_courses.py`. The first module of each path currently includes an authored introduction, definition, reason to learn it, and five practical examples. Topic completion is stored in the `career_topic_progress` SQLite table and is tracked separately per learner and course.

**Implementation status:** this phase adds course navigation, curriculum maps, introductory examples, and saved topic checkmarks. It does not yet claim that every listed topic has a full lesson, randomized quiz, timed module examination, project lab, revision center, or certificate. Those require subsequent content and assessment phases.

Run the application from this directory after installing dependencies:

```powershell
python -m pip install -r requirements.txt
python app.py
```
