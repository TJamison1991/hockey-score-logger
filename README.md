# HOCKEY SCORE LOGGER

This project is meant to act as a hockey score logger that highlights the full understanding and use of CRUD. This project contains contains an HTML page designed to log hockey scores with the option to CREATE, READ, UPDATE, and DELETE.

## Features
- Contains a table on a webpage (LocalHost:5000)
- Fully functional table
- Ability to add, update, delete games

## Project Structure
```
hockey-score-logger/
├── app.py
├── requirements.txt
├── database.py
├── README.md
├── .gitignore
├── data/
│   └── practice.db
└── static/
└── templates/
    ├── index.html
    ├── add_game.html
    └── update_game.html
```
## How To Install And Run
- Clone the repo from GitHub
    git clone <repository-url>
- Navigate to hockey-score-logger
- Install dependencies
    pip install -r requirements.txt
- Set up the database
    python database.py
- Run the app
    python app.py
- Visit the site
    type "LocalHost:5000" in your browser

## Technologies Used
- Python 3
- Flask - web framework
- SQLite - database storage
- HTML - frontend interface

## What I Learned
I learned how to build and write HTML. I'm also learning and understanding CRUD and how to incorporate it within projects. Throughout this project, I also learned how to better set up a repo structure to help myself remain organized. When creating the webpage, I learned how to use Flask along with a request/response cycle as well as GET and POST. Also how to utilize CRUD for updating, adding, deleting data from the table found on the webpage. If I continued on with this, I would like to add more games and potentially make the page look a little more inviting