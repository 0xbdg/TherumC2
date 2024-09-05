from app import *
from flask_wtf import wtforms, FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm): 
    username = StringField(validators=[InputRequired(), Length(min=0, max=255)], render_kw={'placeholder':'username'})
    password = PasswordField(validators=[InputRequired(), Length(min=0, max=255)], render_kw={'placeholder':'password'})

    submit = SubmitField('Login')