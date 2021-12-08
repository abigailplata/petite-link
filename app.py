import sqlite3

from hashids import Hashids
from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET KEY'] = 'O731'

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=('GET','POST'))
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is required.')
            return redirect(url_for('index'))
        url_data = conn.execute('INSERT TO urls (original_url) VALUES (?)',(url,))
        conn.commit()
        conn.close()

        url_id = url_data.lastrowid
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

#@app.route('/getshortlink')
#def getshortlink():

