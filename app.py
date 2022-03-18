from flask import Flask, render_template
import sqlite3
import json
from Models import artists

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def welcome(name):
    return json.dumps( {'name' : name }), 200

if __name__ == "__main__":
    # Setup sqlite db connection objects
    con = sqlite3.connect('test.db')
    cur = con.cursor()

    # Add a new record to the 'artists' table
    dumb_name = "weinerschnitzel3"
    fake_artist = artists.Artist(cur, -1, dumb_name)
    print(fake_artist.ToDict())
    fake_artist.SendToDb()
    con.commit()

    # Read that record back
    cur = con.cursor()
    res = cur.execute(f"select * from artists WHERE Name = '{dumb_name}'").fetchone()
    print(res)

    con.close()
    app.run(host='0.0.0.0', port=8005)