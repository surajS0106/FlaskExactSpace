# app.py

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def init_sqlite_db():
    with sqlite3.connect('db.sqlite3') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT NOT NULL);')
        conn.commit()

init_sqlite_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    with sqlite3.connect('db.sqlite3') as conn:
        if request.method == 'POST':
            note = request.form.get('note')
            conn.execute('INSERT INTO notes (content) VALUES (?)', (note,))
            conn.commit()
        
        all_notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=all_notes)

if __name__ == '__main__':
    app.run(debug=True)
