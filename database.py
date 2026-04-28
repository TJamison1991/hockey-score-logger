import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "practice.db")

def create_tables():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games(
                   game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   home_team TEXT NOT NULL,
                   away_team TEXT NOT NULL,
                   home_score INTEGER,
                   away_score INTEGER,
                   date_played TEXT NOT NULL,
                   status TEXT NOT NULL
        )"""
    )

    connection.commit()
    connection.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()