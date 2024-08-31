import sqlite3
import random
import string
import os
import hashlib


# Get the directory where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the database file
db_path = os.path.join(base_dir, 'exercises.db')

exercise6_column = ""


def get_db():
    global db_path
    # Return a new connection for each request
    return sqlite3.connect(db_path)


def restart_database():
    global exercise6_column

    print("Restarting SQLite database")
    db = get_db()
    cursor = db.cursor()

    # Reset tables
    cursor.execute('DROP TABLE IF EXISTS exercise1;')
    cursor.execute('DROP TABLE IF EXISTS exercise3;')
    cursor.execute('DROP TABLE IF EXISTS exercise4;')
    cursor.execute('DROP TABLE IF EXISTS secret_exercise4;')
    cursor.execute('DROP TABLE IF EXISTS exercise6_super_secret_table;')
    cursor.execute('DROP TABLE IF EXISTS exercise7;')
    
    cursor.execute('''
        CREATE TABLE exercise1 (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    flag = 'FLAG{' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32)) + '}'
    cursor.execute(f'''
        INSERT INTO exercise1 (username, password) VALUES
        ('user', 'eef4d9dafcf027232915d5d41d51741f'),
        ('admin', '35add69719391a43779dbf513aa17001'),
        ('flag_{res}', '{flag}')
    ''')


    cursor.execute('''
        CREATE TABLE exercise3 (
            id INTEGER PRIMARY KEY,
            job_title  TEXT NOT NULL
        )
    ''')

    flag = 'FLAG{' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32)) + '}'
    cursor.execute(f'''
        INSERT INTO exercise3 (job_title) VALUES 
        ('Cybersecurity Analyst'),
        ('Cybersecurity Engineer'),
        ('Cybersecurity Consultant'),
        ('Cybersecurity Architect'),
        ('Cybersecurity Specialist'),
        ('Cybersecurity Manager'),
        ('Cybersecurity Director'),
        ('Cybersecurity Researcher'),
        ('Cybersecurity Incident Responder'),
        ('Cybersecurity Threat Analyst'),
        ('{flag}')
    ''')


    cursor.execute('''
        CREATE TABLE exercise4 (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE secret_exercise4 (
            secret_id INTEGER PRIMARY KEY,
            secret_info TEXT,
            secret_value TEXT
        )
    ''')

    flag = 'FLAG{' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32)) + '}'
    cursor.execute(f'''
        INSERT INTO exercise4 (name, email) VALUES 
        ('Alice Johnson', 'alice@example.com'),
        ('Bob Smith', 'bob@example.com'),
        ('Charlie Brown', 'charlie@example.com'),
        ('Diana Prince', 'diana@example.com');
    ''')

    cursor.execute(f'''
        INSERT INTO secret_exercise4 (secret_info, secret_value) VALUES 
        ('Secret API Key', '12345-ABCDE'),
        ('Admin Password', 'admin123'),
        ('flag', '{flag}'),
        ('Encryption Key', 'abcdefghijklmnopqrstuvwxyz')
    ''')


    exercise6_column = 'column_'+''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    flag = 'FLAG{' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32)) + '}'
    cursor.execute(f'''
        CREATE TABLE exercise6_super_secret_table (
            id INTEGER PRIMARY KEY,
            {exercise6_column} TEXT
        )
    ''')

    cursor.execute(f'''
        INSERT INTO exercise6_super_secret_table ({exercise6_column}) VALUES 
        ('{flag}')
    ''')


    cursor.execute('''
        CREATE TABLE exercise7 (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            stock INTEGER NOT NULL
        );
    ''')

    cursor.execute('''
        INSERT INTO exercise7 (id, product_name, stock) VALUES
        (1, 'Laptop', 0),
        (2, 'Smartphone', 12),
        (3, 'Tablet', 0),
        (4, 'Headphones', 20),
        (5, 'Smartwatch', 0);
    ''')


    # Commit changes and close the connection
    db.commit()
    cursor.close()
    db.close()


def handle_flag(cursor, exercise, flag_input):
    global exercise6_column
    try:
        match exercise:
            case 1:
                flag = cursor.execute("SELECT password FROM exercise1 WHERE username LIKE 'flag_%'").fetchone()[0]
                return "Congratulations! Level solved." if (flag == flag_input) else "Wrong flag."

            case 3:
                flag = cursor.execute("SELECT job_title FROM exercise3 WHERE job_title LIKE 'FLAG{%'").fetchone()[0]
                return "Congratulations! Level solved." if (flag == flag_input) else "Wrong flag."

            case 4:
                flag = cursor.execute("SELECT secret_value FROM secret_exercise4 WHERE secret_info = 'flag'").fetchone()[0]
                return "Congratulations! Level solved." if (flag == flag_input) else "Wrong flag."

            case 5:
                flag = cursor.execute("SELECT sqlite_version()").fetchone()[0]
                return "Congratulations! Level solved." if (flag == flag_input) else "Wrong flag."

            case 6:
                flag = cursor.execute("SELECT "+exercise6_column+" FROM exercise6_super_secret_table").fetchone()[0]
                return "Congratulations! Level solved." if (flag == flag_input) else "Wrong flag."

            case _:
                return "What is happening?"
                
    except sqlite3.Error as e:
        return f"Error: {e}"
    

def get_md5(password):
    md5_value = hashlib.md5(bytes(password,'utf-8'))
    return md5_value.hexdigest()