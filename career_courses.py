"""Roadmap data for the Java, DevOps and SQL CODEQUEST learning paths.
The first module in each course includes authored starter lessons; later modules
are represented as explicit curriculum maps for phased content expansion.
"""

COURSES = {
    "java": {
        "slug": "java", "name": "Java Empire", "icon": "☕", "tagline": "Build strong foundations, then create production-ready Java applications.",
        "level": "Absolute Beginner → Job Ready", "modules": [
            ("Programming and Java Foundations", ["Introduction to Programming", "Introduction to Java", "History and Features of Java", "Java Applications", "JDK, JRE and JVM", "Java Installation", "VS Code and IntelliJ IDEA Setup", "First Java Program", "Java Program Structure", "Compilation and Execution", "Comments", "Keywords and Identifiers", "Variables and Constants", "Primitive Data Types", "Non-Primitive Data Types", "Type Casting", "User Input and Output", "Scanner Class"]),
            ("Operators and Conditional Statements", ["Arithmetic Operators", "Assignment Operators", "Relational Operators", "Logical Operators", "Unary Operators", "Bitwise Operators", "Ternary Operator", "Operator Precedence", "if Statement", "if-else", "Nested if", "else-if Ladder", "Switch Statement", "Enhanced Switch"]),
            ("Loops and Patterns", ["for Loop", "while Loop", "do-while Loop", "Nested Loops", "break", "continue", "return", "Number Patterns", "Star Patterns", "Pyramid Patterns", "Loop-Based Coding Problems"]),
            ("Arrays and Strings", ["One-Dimensional Arrays", "Two-Dimensional Arrays", "Multidimensional Arrays", "Array Traversal", "Searching Algorithms", "Sorting Algorithms", "Linear Search", "Binary Search", "Bubble Sort", "Selection Sort", "Insertion Sort", "String Creation", "String Methods", "String Pool", "String Immutability", "StringBuilder", "StringBuffer", "Palindrome and Anagram Programs"]),
            ("Methods and OOP", ["Methods", "Parameters and Arguments", "Return Types", "Method Overloading", "Recursion", "Classes and Objects", "Constructors", "this Keyword", "static Keyword", "final Keyword", "Encapsulation", "Inheritance", "Polymorphism", "Abstraction", "Abstract Classes", "Interfaces", "Access Modifiers", "Packages", "Inner Classes"]),
            ("Exception Handling and Collections", ["Exception Hierarchy", "Checked and Unchecked Exceptions", "try-catch", "finally", "throw and throws", "Custom Exceptions", "Collections Framework", "List", "ArrayList", "LinkedList", "Vector", "Stack", "Set", "HashSet", "TreeSet", "Map", "HashMap", "LinkedHashMap", "TreeMap", "Queue", "Iterator", "Comparable and Comparator"]),
            ("Advanced Java", ["Generics", "Lambda Expressions", "Functional Interfaces", "Stream API", "Optional Class", "Date and Time API", "Multithreading", "Thread Lifecycle", "Runnable Interface", "Synchronization", "Executor Framework", "File Handling", "Serialization", "Deserialization", "Java I/O and NIO"]),
            ("JDBC and Database Integration", ["JDBC Introduction", "JDBC Architecture", "Database Connectivity", "Statement", "PreparedStatement", "ResultSet", "CRUD Operations", "Transactions", "MySQL Integration", "Database Projects"]),
            ("Spring and Spring Boot", ["Spring Framework", "Dependency Injection", "Inversion of Control", "Spring Beans", "Spring MVC", "Spring Boot", "REST API Development", "GET, POST, PUT and DELETE", "Spring Data JPA", "Hibernate", "Entity Relationships", "Spring Security", "Authentication and Authorization", "JWT", "Validation", "Microservices Introduction", "Postman API Testing"]),
            ("Testing and Professional Development", ["Debugging", "Logging", "JUnit", "Mockito", "Unit Testing", "Maven", "Gradle", "Git and GitHub", "SOLID Principles", "Design Patterns", "JVM Internals", "Memory Management", "Garbage Collection", "Deployment", "Docker Introduction"]),
            ("Data Structures and Algorithms", ["Time and Space Complexity", "Big O Notation", "Arrays", "Strings", "Linked Lists", "Stacks", "Queues", "Hashing", "Trees", "Binary Search Trees", "Heaps", "Graphs", "BFS and DFS", "Recursion", "Backtracking", "Greedy Algorithms", "Dynamic Programming"]),
            ("Java Interview and Projects", ["Core Java interview questions", "OOP interview questions", "Collections questions", "Multithreading questions", "Java coding rounds", "JDBC questions", "Spring Boot interview questions", "Calculator project", "Student Management System", "Banking Application", "Library Management System", "Employee Management System", "Online Examination System", "Spring Boot REST API", "E-commerce Backend", "Job Portal Application"]),
        ],
        "intro": "Java is a strongly typed, object-oriented language used to build backend services, Android applications and enterprise systems.",
        "definition": "Java source code is compiled into bytecode that runs on a Java Virtual Machine (JVM). This design supports portability across systems with a compatible JVM.",
        "why": "Java teaches programming fundamentals, object-oriented design, type safety and maintainable application development.",
        "examples": [
            ("Your first output", 'class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, CODEQUEST!");\n    }\n}', 'System.out.println displays a line of text in the console.'),
            ("Store a value", 'class Main {\n    public static void main(String[] args) {\n        String hero = "Mira";\n        System.out.println(hero);\n    }\n}', 'String stores text; hero is the variable name.'),
            ("Work with numbers", 'class Main {\n    public static void main(String[] args) {\n        int coins = 12;\n        int bonus = 5;\n        System.out.println(coins + bonus);\n    }\n}', 'int stores whole numbers and + adds them.'),
            ("Make a decision", 'class Main {\n    public static void main(String[] args) {\n        int score = 80;\n        if (score >= 50) {\n            System.out.println("Pass");\n        }\n    }\n}', 'The if block runs when its condition evaluates to true.'),
            ("Repeat an action", 'class Main {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 3; i++) {\n            System.out.println(i);\n        }\n    }\n}', 'The for loop prints 1, 2 and 3.')
        ]
    },
    "devops": {
        "slug": "devops", "name": "DevOps Universe", "icon": "🚀", "tagline": "Connect development and operations through automation and reliable delivery.",
        "level": "Absolute Beginner → Professional", "modules": [
            ("Introduction to DevOps", ["What is DevOps?", "Why DevOps?", "Traditional Software Development", "DevOps Lifecycle", "DevOps Culture", "DevOps Principles", "CI and CD", "Continuous Integration", "Continuous Delivery", "Continuous Deployment", "DevOps Engineer Responsibilities", "DevOps Tools Overview"]),
            ("Linux Fundamentals", ["Introduction to Linux", "Linux Architecture", "Linux Distributions", "Ubuntu Installation", "WSL Setup on Windows", "Linux Terminal", "pwd", "ls", "cd", "mkdir", "touch", "cat", "cp", "mv", "rm", "File Permissions", "chmod", "chown", "Users and Groups", "sudo", "grep", "find", "head and tail", "Pipes", "Redirection", "Process Management", "ps", "top", "kill", "Package Management", "apt", "Environment Variables", "Shell Scripting Basics", "Bash Automation", "Linux Networking Commands", "SSH", "Cron Jobs", "Log Management"]),
            ("Networking Fundamentals", ["Computer Networks", "IP Address", "Public and Private IP", "MAC Address", "DNS", "DHCP", "TCP and UDP", "HTTP and HTTPS", "OSI Model", "TCP/IP Model", "Ports", "Firewalls", "Subnets", "Routing", "Load Balancing", "Proxy and Reverse Proxy", "SSH and SFTP", "Networking Troubleshooting"]),
            ("Git and GitHub", ["Version Control", "Git Installation", "Git Configuration", "git init", "git status", "git add", "git commit", "git log", "git diff", "git push", "git pull", "git clone", "Branches", "Merging", "Merge Conflicts", "Pull Requests", "Forking", "GitHub Repositories", "GitHub Actions", "Git Best Practices"]),
            ("Python and Shell Scripting", ["Bash Scripting", "Variables", "Conditions", "Loops", "Functions", "File Automation", "User Input", "Error Handling", "Scheduling Scripts", "Python Fundamentals for Automation", "Python File Handling", "Python OS Module", "Subprocess Module", "API Automation", "Log Monitoring Scripts", "Server Health Check Automation"]),
            ("Build and Package Management", ["Software Build Process", "Compilation", "Maven", "Maven Installation", "pom.xml", "Maven Lifecycle", "Maven Dependencies", "Maven Build", "Gradle", "Artifact Management", "JAR and WAR Files", "Nexus Repository", "JFrog Artifactory"]),
            ("Jenkins and CI/CD", ["Jenkins Introduction", "Jenkins Architecture", "Jenkins Installation", "Jenkins Dashboard", "Jenkins Jobs", "Freestyle Projects", "Jenkins Pipeline", "Jenkinsfile", "Pipeline Syntax", "Build Triggers", "Webhook Integration", "GitHub Integration", "Maven Integration", "Automated Testing", "Build and Deployment Pipelines", "Jenkins Credentials", "Agents and Nodes", "Pipeline Troubleshooting", "CI/CD Best Practices"]),
            ("Docker and Containerization", ["Containers", "Virtual Machines vs Containers", "Docker Architecture", "Docker Installation", "Docker Engine", "Docker Images", "Docker Containers", "Dockerfile", "Docker Commands", "Docker Build", "Docker Run", "Docker Exec", "Docker Volumes", "Docker Networks", "Docker Compose", "Multi-Container Applications", "Docker Registry", "Docker Hub", "Container Optimization", "Docker Security"]),
            ("Kubernetes", ["Kubernetes Introduction", "Kubernetes Architecture", "Master and Worker Nodes", "Pods", "Deployments", "ReplicaSets", "Services", "ConfigMaps", "Secrets", "Namespaces", "Labels and Selectors", "Volumes", "Persistent Volumes", "Persistent Volume Claims", "Ingress", "Helm", "kubectl Commands", "Scaling Applications", "Rolling Updates", "Rollbacks", "Troubleshooting", "Kubernetes Security", "Monitoring"]),
            ("Cloud Computing and AWS", ["Cloud Computing", "IaaS, PaaS and SaaS", "Public, Private and Hybrid Cloud", "AWS Introduction", "AWS Global Infrastructure", "IAM", "EC2", "S3", "VPC", "Subnets", "Security Groups", "Route 53", "Load Balancers", "Auto Scaling", "RDS", "CloudWatch", "ECR", "ECS", "EKS", "AWS CLI", "AWS Deployment", "Cloud Security", "AWS Cost Management"]),
            ("Infrastructure as Code", ["IaC Introduction", "Terraform", "Terraform Installation", "Providers", "Resources", "Variables", "Outputs", "State Files", "Terraform Plan", "Terraform Apply", "Terraform Destroy", "Modules", "Remote State", "Terraform with AWS", "Ansible", "Ansible Architecture", "Inventory", "Playbooks", "Variables", "Roles", "Configuration Management"]),
            ("Monitoring and Logging", ["Monitoring Fundamentals", "Metrics and Logs", "Prometheus", "Prometheus Architecture", "Exporters", "Grafana", "Dashboards", "Alerts", "Alertmanager", "ELK Stack", "Elasticsearch", "Logstash", "Kibana", "Centralized Logging", "Application Monitoring", "Server Monitoring", "Incident Management"]),
            ("DevSecOps and Security", ["DevSecOps Introduction", "Secure CI/CD", "Secrets Management", "IAM Best Practices", "Docker Security", "Kubernetes Security", "Vulnerability Scanning", "Dependency Scanning", "SonarQube", "SAST and DAST", "Security Policies", "Compliance Basics"]),
            ("Advanced DevOps and SRE", ["Microservices Architecture", "Service Discovery", "API Gateway", "Blue-Green Deployment", "Canary Deployment", "Rolling Deployment", "High Availability", "Disaster Recovery", "Backup Strategies", "Site Reliability Engineering", "SLIs, SLOs and SLAs", "Incident Response", "Capacity Planning", "Performance Optimization", "Production Troubleshooting"]),
            ("DevOps Projects and Interviews", ["Linux Server Monitoring", "Automated Backup System", "GitHub-Jenkins CI/CD Pipeline", "Dockerized Java Application", "Dockerized Python Application", "Kubernetes Deployment", "AWS Web Application Deployment", "Terraform Infrastructure Provisioning", "Ansible Server Automation", "Prometheus and Grafana Monitoring", "End-to-End DevOps Pipeline", "Linux interview questions", "Networking scenarios", "CI/CD troubleshooting", "Cloud and Kubernetes interviews"]),
        ],
        "intro": "DevOps combines development practices, operations knowledge and automation to deliver software reliably and frequently.",
        "definition": "DevOps is a culture and set of practices that improve collaboration, automation, feedback and shared responsibility across the software lifecycle.",
        "why": "Teams use DevOps to reduce manual handoffs, detect failures earlier, shorten delivery cycles and improve service reliability.",
        "examples": [
            ("Check your current folder", "pwd", "pwd prints the current working directory in a Linux shell."),
            ("List files", "ls -la", "ls lists directory contents; -la includes hidden files and details."),
            ("Create a practice folder", "mkdir -p ~/devops-lab/logs", "mkdir creates directories; -p also creates missing parent directories."),
            ("Write a sample log", "echo 'Build completed' > build.log\ncat build.log", "The > operator redirects output into a file, replacing its previous contents."),
            ("Inspect a running process", "ps -ef | head", "The pipe sends ps output to head, which displays the first lines.")
        ]
    },
    "sql": {
        "slug": "sql", "name": "SQL Underworld", "icon": "🗄️", "tagline": "Query, design and optimize databases with practical SQL skills.",
        "level": "Absolute Beginner → Job Ready", "modules": [
            ("Database Fundamentals", ["What is Data?", "What is a Database?", "DBMS Introduction", "RDBMS Introduction", "SQL Introduction", "SQL vs MySQL", "Database Architecture", "Tables, Rows and Columns", "Primary Keys", "Foreign Keys", "Relationships", "Database Installation", "MySQL Workbench Setup", "PostgreSQL Introduction"]),
            ("SQL Basics", ["CREATE DATABASE", "DROP DATABASE", "USE DATABASE", "CREATE TABLE", "ALTER TABLE", "DROP TABLE", "TRUNCATE TABLE", "INSERT", "SELECT", "DISTINCT", "UPDATE", "DELETE", "WHERE", "ORDER BY", "LIMIT", "OFFSET", "Aliases"]),
            ("SQL Operators", ["Arithmetic Operators", "Comparison Operators", "Logical Operators", "AND", "OR", "NOT", "BETWEEN", "IN", "NOT IN", "LIKE", "Wildcards", "IS NULL", "IS NOT NULL"]),
            ("SQL Functions", ["Aggregate Functions", "COUNT", "SUM", "AVG", "MIN", "MAX", "String Functions", "CONCAT", "LENGTH", "UPPER", "LOWER", "SUBSTRING", "TRIM", "Numeric Functions", "ROUND", "CEIL", "FLOOR", "Date Functions", "NOW", "DATE", "DATEDIFF", "CASE Statements"]),
            ("Grouping and Filtering", ["GROUP BY", "HAVING", "WHERE vs HAVING", "Aggregate Filtering", "Multiple Column Grouping", "Conditional Aggregation", "Real-World Reporting Queries"]),
            ("SQL Joins", ["Introduction to Joins", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN", "CROSS JOIN", "SELF JOIN", "Multiple Table Joins", "Joining Three or More Tables", "Real-World Join Problems"]),
            ("Subqueries and Advanced Queries", ["Subqueries", "Single-Row Subqueries", "Multiple-Row Subqueries", "Correlated Subqueries", "Nested Queries", "EXISTS", "NOT EXISTS", "ANY", "ALL", "Common Table Expressions", "WITH Clause", "Recursive CTEs", "Window Functions", "ROW_NUMBER", "RANK", "DENSE_RANK", "LEAD", "LAG", "PARTITION BY", "OVER Clause"]),
            ("Database Design and Normalization", ["Database Design", "ER Diagrams", "Entities and Attributes", "Relationships", "One-to-One", "One-to-Many", "Many-to-Many", "Functional Dependencies", "First Normal Form", "Second Normal Form", "Third Normal Form", "BCNF", "Denormalization", "Database Design Best Practices"]),
            ("Constraints and Indexes", ["NOT NULL", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY", "CHECK", "DEFAULT", "Composite Keys", "Indexes", "Clustered and Non-Clustered Index Concepts", "Unique Indexes", "Composite Indexes", "Index Optimization", "Query Performance"]),
            ("Transactions and Stored Programs", ["Transactions", "ACID Properties", "COMMIT", "ROLLBACK", "SAVEPOINT", "Isolation Levels", "Concurrency", "Deadlocks", "Stored Procedures", "Functions", "Triggers", "Cursors", "Views", "Materialized Views"]),
            ("SQL Performance and Optimization", ["Query Execution", "Execution Plans", "EXPLAIN", "Query Optimization", "Index Selection", "Slow Query Analysis", "Joins Optimization", "Subquery Optimization", "Database Performance Monitoring", "SQL Best Practices"]),
            ("SQL with Programming Languages", ["SQL with Python", "SQL with Java", "JDBC", "Python Database Connectivity", "CRUD Applications", "Database APIs", "SQL with Flask", "SQL with Spring Boot", "ORM Introduction", "Hibernate and JPA"]),
            ("Practical SQL Projects", ["Student Database", "Employee Database", "Library Database", "Banking Database", "E-commerce Database", "Hospital Management Database", "Inventory Management Database", "Sales Analysis", "HR Analytics", "Customer Analytics Dashboard"]),
            ("SQL Interview Preparation", ["Basic SQL Interview Questions", "Intermediate SQL Questions", "Advanced SQL Questions", "Joins Interview Questions", "Subquery Problems", "Window Function Questions", "Query Optimization Questions", "Database Design Questions", "Real-World SQL Scenarios", "SQL Coding Assessments"]),
        ],
        "intro": "SQL (Structured Query Language) is used to define, read, change and manage data in relational databases.",
        "definition": "A relational database stores data in tables. SQL statements communicate with the database to query data and manage its structure and records.",
        "why": "SQL is essential for application development, reporting, data analytics, testing and understanding business information.",
        "examples": [
            ("Create a database", "CREATE DATABASE codequest_lab;", "Creates a database named codequest_lab. Run this in a SQL client with permission to create databases."),
            ("Create a table", "CREATE TABLE students (\n    student_id INT PRIMARY KEY,\n    name VARCHAR(80),\n    score INT\n);", "CREATE TABLE defines columns and a primary key for each student row."),
            ("Insert a row", "INSERT INTO students (student_id, name, score)\nVALUES (1, 'Mira', 92);", "INSERT adds one record by naming its columns and supplying matching values."),
            ("Read records", "SELECT name, score\nFROM students\nWHERE score >= 80\nORDER BY score DESC;", "SELECT retrieves chosen columns, WHERE filters rows and ORDER BY sorts the result."),
            ("Summarize records", "SELECT COUNT(*) AS student_count, AVG(score) AS average_score\nFROM students;", "COUNT and AVG calculate aggregate values over the selected rows.")
        ]
    }
}

for course in COURSES.values():
    course["modules"] = [
        {"id": i, "title": title, "topics": topics,
         "intro": f"Study {title.lower()} through {len(topics)} focused topics and practical checkpoints."}
        for i, (title, topics) in enumerate(course["modules"], 1)
    ]
