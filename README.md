# SQL-InjectEducation
SQL Injection guided labs to learn the basics.


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

## More Info

### Source Code Directory structure
```csharp
sql_injecteducation/
│
├── app.py              # Main Flask application
├── exercises.db        # SQLite database
├── exercises/          # Directory for exercise files
│   ├── sqlite_exercises.py    # Code for SQLite exercise 1
│   └── postgresql_exercises.py # Code for PostgreSQL exercise 1
├── static/             # For static files (e.g., CSS, JS)
│   └── style.css       # Custom CSS
├── templates/          # For HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Homepage with sections
│   └── exercise.html   # Exercise page
└── venv/               # Virtual environment (optional)

```