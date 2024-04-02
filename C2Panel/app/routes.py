from flask import render_template, request
from app import app

@app.route('/')
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")