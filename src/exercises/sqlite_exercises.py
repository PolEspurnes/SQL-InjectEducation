from flask import render_template, request, g
import sqlite3
import random
import string


def get_db():
    conn = sqlite3.connect('exercises.db')
    return conn.cursor()
    

def sqlite_exercise1():
    db = get_db()
    exercise = {
        'name': 'Simple Injection',
        'description': 'Try a basic SQL injection on the users table and get the flag from the flag user.'
    }

    result = ""
    query = ""
    if request.method == 'POST':
        if 'user_input' in request.form:
            user_input = request.form['user_input']
            # Vulnerable SQL query for educational purposes
            query = f"SELECT * FROM exercise1 WHERE username = '{user_input}'"
            try:
                cur = db.execute(query)
                result = cur.fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

            
        elif 'flag_input' in request.form:
            flag = request.form['flag_input']
            # Process the flag as needed (e.g., store it, check it, etc.)
            print(f"Flag submitted: {flag}")
            # You can add specific flag handling logic here if needed
            result = f"Congratulations! Level solved. {flag}"

        return render_template('exercise.html', exercise=exercise, result=result, query=query)

    return render_template('exercise.html', exercise=exercise)


def sqlite_exercise2():
    db = get_db()
    exercise = {
        'name': 'Simple Login Bypass Injection',
        'description': 'Try a basic SQL injection on a login panel and bypass the authentication.'
    }

    if request.method == 'POST':
        user_input = request.form['user_input']
        # Vulnerable SQL query for educational purposes
        query = f"SELECT * FROM users WHERE username = '{user_input}'"
        try:
            cur = db.execute(query)
            result = cur.fetchall()
        except sqlite3.Error as e:
            result = f"Error: {e}"

        return render_template('exercise.html', exercise=exercise, result=result, query=query)

    return render_template('exercise.html', exercise=exercise)


def sqlite_exercise3():
    db = get_db()
    exercise = {
        'name': 'Login Bypass Injection',
        'description': 'Try a basic SQL injection on a login panel and bypass the authentication.'
    }

    if request.method == 'POST':
        if 'user_input' in request.form:
            user_input = request.form['user_input']
            # Vulnerable SQL query for educational purposes
            query = f"SELECT * FROM users WHERE username = '{user_input}'"
            try:
                cur = db.execute(query)
                result = cur.fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

            
        elif 'flag_submit' in request.form:
            flag = request.form.get('flag', '')
            # Process the flag as needed (e.g., store it, check it, etc.)
            print(f"Flag submitted: {flag}")
            # You can add specific flag handling logic here if needed
            result = "Congratulations! Level solved."

        return render_template('exercise.html', exercise=exercise, result=result, query=query)

    return render_template('exercise.html', exercise=exercise)



def restart_database():
    print("Restaring sqlite db")
    db = get_db()
    # Reset table
    db.execute('DROP TABLE IF EXISTS exercises;')
    
    # Create a table for exercises
    db.execute('''
        CREATE TABLE exercises (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            table_name TEXT NOT NULL,
            field_name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    # Add a sample exercise
    db.execute('''
        INSERT INTO exercises (name, table_name, field_name, description) 
        VALUES ('Simple Injection', 'users', 'username', 'Try a basic SQL injection on the users table.')
    ''')

    # Reset table
    db.execute('DROP TABLE IF EXISTS exercise1;')
    
    ## Create a sample users table in the same database:
    db.execute('''
        CREATE TABLE exercise1 (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    flag = 'FLAG{'+''.join(random.choices(string.ascii_uppercase + string.digits, k=32))+'}'
    db.execute(f'''
        INSERT INTO exercise1 (username, password) VALUES
        ('admin', '35add69719391a43779dbf513aa17001'),
        ('user', 'eef4d9dafcf027232915d5d41d51741f'),
        ('flag_{res}', '{flag}')
    ''')
