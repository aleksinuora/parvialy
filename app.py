from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/login", methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # tarkista kirjautumistiedot tässä
    session["username"] = username
    return redirect("/")

@app.route("/user/<username>")
def user(username):
    return render_template("todo.html")

@app.route("/result", methods = ["POST"])
def result():
    return render_template("todo.html")

@app.route("/test")
def test():
    sql1 = "SELECT content FROM test"
    sql2 = "INSERT INTO test (content) VALUES ('lisäys toimii')"
    db.session.execute(sql2)
    result = db.session.execute(sql1)
    result1 = [r['content'] for r in result]
    result2 = result1[0]
    result3 = "lisäys bugaa"
    if len(result1) > 1:
         result3 = result1[1]
         db.session.execute("DELETE FROM test WHERE id > 1")
    return render_template("/test.html", result2=result2, result3=result3)
