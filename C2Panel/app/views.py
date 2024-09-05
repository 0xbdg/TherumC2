from flask import render_template, request
from flask_login import login_required
from app import *
from app.forms import LoginForm
from app.models import Users

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("pages/login.html", form=form)

@app.route("/home", methods=["GET"])
@login_required
def index():
    return render_template("pages/home.html")