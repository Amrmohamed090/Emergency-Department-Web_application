from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=1, max=30)])
    submit = SubmitField('Login')
    remember = BooleanField('remember Me')


class Signup_DoctorForm(FlaskForm):
    
    Fname = StringField('First-name', validators=[DataRequired(), Length(min=2, max=20)])
    
    Lname = StringField('Last-name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    degree = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired(), Length(min=5, max=30)])
    speciallity = StringField('Major-Scientific-area', validators=[DataRequired(), Length(min=5, max=30)])
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=30)])
    submit = SubmitField('sign up')
