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

@app.route("/add", methods=["GET", "POST"])
def add_game():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if request.method == "POST":
        home_team = request.form["home_team"]
        away_team = request.form["away_team"]
        date_played = request.form["date_played"]
        status = request.form["status"]
        cursor.execute("""
            INSERT INTO games (home_team, away_team, home_score, away_score, date_played, status)
            VALUES (?, ?, 0, 0, ?, ?)
        """, (home_team, away_team, date_played, status))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    else:
        conn.close()
        return render_template("add_game.html")
    
@app.route("/update/<game_id>", methods=["GET", "POST"])
def update_game(game_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if request.method == "POST":
        home_score = request.form["home_score"]
        away_score = request.form["away_score"]
        status = request.form["status"]
        cursor.execute("""
            UPDATE games SET home_score = ?, away_score = ?, status = ? WHERE game_id = ?
        """, (home_score, away_score, status, game_id))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    else:
        conn.close()
        return render_template("update_game.html", game_id=game_id)


if __name__ == "__main__":
    app.run(debug=True)