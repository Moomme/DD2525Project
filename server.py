# To run server
# $ export FLASK_APP=server.py
# $ flask run

import sqlite3
from flask import Flask
from flask import request

app = Flask(__name__)

DATABASE = './database.db'

def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, one=False):
    cur = get_db().execute(query)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/isuser')
def index():
    username = request.args.get('username')
    q = "select * from users where username='" + username + "'"
    print(q)

    user = query_db(q, one=True)
    if user is None:
        return 'No such user\n'
    else:
        return username + ' is a user\n'
