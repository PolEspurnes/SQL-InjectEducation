from flask import render_template, request
from utils.db_sqlite import *



def sqlite_exercise1():
    result = ""
    query = ""

    exercise = {
        'name': 'Simple Injection',
        'description': 'Try a basic SQL injection on the users table and get the flag from the flag user.'
    }


    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        # User input
        if 'user_input' in request.form:
            user_input = request.form['user_input']

            query = f"SELECT * FROM exercise1 WHERE username = '{user_input}'"
            try:
                result = cursor.execute(query).fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

        # Flag input
        elif 'flag_input' in request.form:
            flag_input = request.form['flag_input']
            result = handle_flag(cursor, 1, flag_input)


        cursor.close()
        db.close()
        return render_template('sqlite_exercise1.html', exercise=exercise, result=result, query=query)

    return render_template('sqlite_exercise1.html', exercise=exercise)


def sqlite_exercise2():
    result = ""
    query = ""

    exercise = {
        'name': 'Simple Login Bypass Injection',
        'description': 'Try a basic SQL injection on a login panel and bypass the authentication to login as "admin".'
    }

    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        username_input = request.form['username'] if 'username' in request.form else ''
        password_input = get_md5(request.form['password']) if 'password' in request.form else ''

        # Vulnerable SQL query for educational purposes
        query = f"SELECT * FROM exercise1 WHERE (username = '{username_input}') AND (password = '{password_input}')"
        try:
            cur = cursor.execute(query)
            result = cur.fetchall()
        except sqlite3.Error as e:
            result = f"Error: {e}"

        cursor.close()
        db.close()
        return render_template('sqlite_exercise2.html', exercise=exercise, result=result, query=query)


    return render_template('sqlite_exercise2.html', exercise=exercise)


def sqlite_exercise3():
    db = get_db()
    cursor = db.cursor()

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
                cur = cursor.execute(query)
                result = cur.fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

        elif 'flag_submit' in request.form:
            flag = request.form.get('flag', '')
            # Process the flag as needed (e.g., store it, check it, etc.)
            print(f"Flag submitted: {flag}")
            result = "Congratulations! Level solved."

        cursor.close()
        db.close()
        return render_template('exercise.html', exercise=exercise, result=result, query=query)

    cursor.close()
    db.close()
    return render_template('exercise.html', exercise=exercise)