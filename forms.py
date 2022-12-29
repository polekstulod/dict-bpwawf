from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, SubmitField


class SignUpForm(FlaskForm):
    age = IntegerField('Age')
    gender = RadioField('Gender', choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Others')])
    team = SelectField('Team', choices=[('red', 'Red'), ('blue', 'Blue'), ('yellow', 'Yellow')])
    submit = SubmitField('Sign up')
