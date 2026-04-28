from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "practice.db")

@app.route("/")
def home():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()
    conn.close()
    return render_template("index.html", games=games)

if __name__ == "__main__":
    app.run(debug=True)