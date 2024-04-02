from flask import render_template, request
from app import app

@app.route('/')
def login():
    return render_template("auth/login.html")

@app.route("/home")
def index():
    return render_template("pages/index.html")