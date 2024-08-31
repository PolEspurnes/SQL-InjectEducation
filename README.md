# SQL-InjectEducation
The SQL InjectEducation Tool is an educational resource designed to help users learn and practice SQL injection techniques using an SQLite database. It features **10 levels with progressive difficulty**, each focusing on **different types of SQL injection vulnerabilities** and attack methods.


## Installation
0. Make sure you have Python 3 installed.

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install Flask and SQLite:
```bash
pip install flask sqlite3
```

## Run
```bash
cd src
python app.py
```

## More Information
- **Lightweight and Easy to Install**: The use of Flask and SQLite ensures that the tool is easy to set up and run on any machine with minimal configuration.

- **Interactive Learning**: Provides hands-on experience with SQL injection techniques with simplified but real examples. The executed queries can always be checked, allowing the user to properly understand what is being executed.

- **Notes and Methodology Section**: Provides detailed guidance and best practices for each level. It is as important to solve the level as it is to understand why the solution worked.