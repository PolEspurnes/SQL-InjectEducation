from flask import render_template, request
from utils.db_sqlite import *



def sqlite_exercise1():
    result = ""
    query = ""

    exercise = {
        'name': 'Simple Injection',
        'description': 'Try a basic SQL injection on the users table and get the flag from exercise1 table.'
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
        query = f"SELECT username FROM exercise1 WHERE (username = '{username_input}') AND (password = '{password_input}')"
        try:
            fetched = cursor.execute(query).fetchone()
            if fetched:
                logged_as = fetched[0]
                result = "Congratulations! Level solved." if (logged_as == "admin") else f"Logged in as {logged_as}, but not admin. Try again."
            else:
                result = "Login failed."
        except sqlite3.Error as e:
            result = f"Error: {e}"

        cursor.close()
        db.close()
        return render_template('sqlite_exercise2.html', exercise=exercise, result=result, query=query)


    return render_template('sqlite_exercise2.html', exercise=exercise)


def sqlite_exercise3():
    result = ""
    query = ""

    exercise = {
        'name': 'LIKE Operator',
        'description': 'Try a basic SQL injection on a query that uses the LIKE operator and get the flag from exercise3 table.',
        'limitation': 'The "-" character is filtered.'
    }

    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        # User input
        if 'user_input' in request.form:
            user_input = request.form['user_input'].replace('-','')

            query = f"SELECT * FROM exercise3 WHERE job_title LIKE 'Cybersecurity {user_input}%'"
            try:
                result = cursor.execute(query).fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

        # Flag input
        elif 'flag_input' in request.form:
            flag_input = request.form['flag_input']
            result = handle_flag(cursor, 3, flag_input)


        cursor.close()
        db.close()
        return render_template('sqlite_exercise3.html', exercise=exercise, result=result, query=query)

    return render_template('sqlite_exercise3.html', exercise=exercise)



def sqlite_exercise4():
    result = ""
    query = ""

    exercise = {
        'name': 'Union-based SQL Injection',
        'description': 'Try a basic Union-based SQL Injection and read the contents of table secret_exercise4.',
        'hint': 'Tables exercise4 and secret_exercise4 have the same amount of columns and column types.'
    }

    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        # User input
        if 'user_input' in request.form:
            user_input = request.form['user_input']

            query = f"SELECT * FROM exercise4 WHERE name LIKE '%{user_input}%'"
            try:
                result = cursor.execute(query).fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

        # Flag input
        elif 'flag_input' in request.form:
            flag_input = request.form['flag_input']
            result = handle_flag(cursor, 4, flag_input)


        cursor.close()
        db.close()
        return render_template('sqlite_exercise4.html', exercise=exercise, result=result, query=query)

    return render_template('sqlite_exercise4.html', exercise=exercise)


def sqlite_exercise5():
    result = ""
    query = ""

    exercise = {
        'name': 'Union-based SQL Injection - Retrieving the sqlite version',
        'description': 'Do a Union-based SQL Injection and read the SQLite version. Send the version as the flag.',
        'hint': 'How can you check the database version in SQLite?'
    }

    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        # User input
        if 'user_input' in request.form:
            user_input = request.form['user_input']

            query = f"SELECT * FROM exercise4 WHERE name LIKE '%{user_input}%'"
            try:
                result = cursor.execute(query).fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

        # Flag input
        elif 'flag_input' in request.form:
            flag_input = request.form['flag_input']
            result = handle_flag(cursor, 5, flag_input)


        cursor.close()
        db.close()
        return render_template('sqlite_exercise4.html', exercise=exercise, result=result, query=query)

    return render_template('sqlite_exercise4.html', exercise=exercise)


def sqlite_exercise6():
    result = ""
    query = ""

    exercise = {
        'name': 'Union-based SQL Injection - Retrieving data from other tables',
        'description': 'Do a Union-based SQL Injection and find the flag contained in the secret table of exercise 6.',
        'hint': 'First find the name of the table, then the columns\' names and finally the flag.'
    }

    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()

        # User input
        if 'user_input' in request.form:
            user_input = request.form['user_input']

            query = f"SELECT * FROM exercise4 WHERE name LIKE '%{user_input}%'"
            try:
                result = cursor.execute(query).fetchall()
            except sqlite3.Error as e:
                result = f"Error: {e}"

        # Flag input
        elif 'flag_input' in request.form:
            flag_input = request.form['flag_input']
            result = handle_flag(cursor, 6, flag_input)


        cursor.close()
        db.close()
        return render_template('sqlite_exercise4.html', exercise=exercise, result=result, query=query)

    return render_template('sqlite_exercise4.html', exercise=exercise)