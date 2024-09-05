from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, template_folder="templates",static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///botnet.db'
app.config['SECRET_KEY'] = 'kontolmemekanjingngentot1234567890!@#$%^&*()_+-?/><.,\|'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
