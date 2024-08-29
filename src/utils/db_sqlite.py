import sqlite3
import random
import string
import os
import hashlib


# Get the directory where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the database file
db_path = os.path.join(base_dir, 'exercises.db')


def get_db():
    global db_path
    # Return a new connection for each request
    return sqlite3.connect(db_path)


def restart_database():
    print("Restarting SQLite database")
    db = get_db()
    cursor = db.cursor()

    # Reset exercise1 table
    cursor.execute('DROP TABLE IF EXISTS exercise1;')
    
    # Create a sample exercise1 table
    cursor.execute('''
        CREATE TABLE exercise1 (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Insert sample data
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    flag = 'FLAG{' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=32)) + '}'
    cursor.execute(f'''
        INSERT INTO exercise1 (username, password) VALUES
        ('user', 'eef4d9dafcf027232915d5d41d51741f'),
        ('admin', '35add69719391a43779dbf513aa17001'),
        ('flag_{res}', '{flag}')
    ''')


    # Commit changes and close the connection
    db.commit()
    cursor.close()
    db.close()


def handle_flag(cursor, exercise, flag_input):
    try:
        match exercise:
            case 1:
                flag = cursor.execute("SELECT password FROM exercise1 WHERE username LIKE 'flag_%'").fetchone()[0]
                return "Congratulations! Level solved." if (flag == flag_input) else "Wrong flag."
            case _:
                return "What is happening?"
                
    except sqlite3.Error as e:
        return f"Error: {e}"
    

def get_md5(password):
    md5_value = hashlib.md5(bytes(password,'utf-8'))
    return md5_value.hexdigest()