from flask import Flask, render_template
from exercises.sqlite_exercises import restart_database, sqlite_exercise1

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise/sqlite1', methods=['GET', 'POST'])
def exercise_sqlite1():
    return sqlite_exercise1()

@app.route('/exercise/postgresql1', methods=['GET', 'POST'])
def exercise_postgresql1():
    # Temporary
    return render_template('index.html')

if __name__ == '__main__':
    restart_database()
    app.run(debug=True)
