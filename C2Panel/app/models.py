from app import db
from sqlalchemy import Column, String, Integer
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), unique=True, nullable=False)

class Zombies(db.Model):
    pass