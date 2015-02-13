# coding=utf8



import sqlite3
from flask import Flask, g, render_template
from models import Entry

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    entries = Entry.gets_all()
    return render_template('index.html', entries=entries)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
