# coding=utf8



import sqlite3
import MySQLdb
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
    g.conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="amazing")

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()




def initdb():
    conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="amazing")
    cur = conn.cursor()
    cur.execute("drop table if exists books")
    cur.execute("drop table if exists chapters")
    cur.execute(
	"create table if not exists books ( "
	"number integer primary key not null, "
	"osis text not null, "
	"human text not null, "
	"chapters integer not null)")

    cur.execute(
	"create table if not exists chapters ( "
	"osis varchar not null, "
	"osis_number int(3) not null, "
	"human varchar not null, "
	"content text not null, "
	"previous_osis varchar, "
	"previous_osis_number int(3) default null, "
	"previous_human varchar, "
	"next_osis varchar, "
	"next_osis_number int(3) default null, "
	"next_human varchar, "
	"primary key (`osis`,`osis_number`), "
	"index `previous_osis_index` (`previous_osis`,`previous_osis_number`), "
	"index `next_osis_index` (`next_osis`,`next_osis_number`))")
    conn.commit()


if __name__ == '__main__':
    #app.run(debug=True)
    initdb()
