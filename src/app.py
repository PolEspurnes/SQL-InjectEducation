from flask import Flask, render_template
from exercises.sqlite_exercises import *
from utils.db_sqlite import restart_database
import sys, signal

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exercise/sqlite1', methods=['GET', 'POST'])
def sqlite1():
    return sqlite_exercise1()


@app.route('/exercise/sqlite2', methods=['GET', 'POST'])
def sqlite2():
    return sqlite_exercise2()


@app.route('/exercise/sqlite3', methods=['GET', 'POST'])
def sqlite3():
    return sqlite_exercise3()


@app.route('/exercise/sqlite4', methods=['GET', 'POST'])
def sqlite4():
    return sqlite_exercise4()


@app.route('/exercise/sqlite5', methods=['GET', 'POST'])
def sqlite5():
    return sqlite_exercise5()


@app.route('/exercise/sqlite6', methods=['GET', 'POST'])
def sqlite6():
    return sqlite_exercise6()


@app.route('/exercise/sqlite7', methods=['GET', 'POST'])
def sqlite7():
    return sqlite_exercise7()


@app.route('/exercise/sqlite8', methods=['GET', 'POST'])
def sqlite8():
    return sqlite_exercise8()


@app.route('/exercise/sqlite9', methods=['GET', 'POST'])
def sqlite9():
    return sqlite_exercise9()


@app.route('/exercise/sqlite10', methods=['GET', 'POST'])
def sqlite10():
    return sqlite_exercise10()


if __name__ == '__main__':
    restart_database()
    app.run(debug=True)
