
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField,IntegerField,DateField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from emergencydebartment.models import Doctor, Patient








class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[
                           DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=1, max=30)])
    submit = SubmitField('Login')
    remember = BooleanField('remember Me')

class RegistrationForm(FlaskForm):
    Fname = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    Sname = StringField('Middle Name', validators=[Length(min=1, max=30)])
    Lname = StringField('Last Name', validators=[DataRequired(),Length(min=1, max=30)])
    ssn = StringField("SSN",  validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    birth_date = DateField('BirthDate')
    gender = RadioField(choices=["male","female"])
    address = StringField('Home address', validators=[DataRequired(), Length(min=1, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=30)])
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('sign up')
    def validate_email(self, email):
        email1 =  Doctor.query.filter_by(email=email.data).first()
        email2 =  Patient.query.filter_by(email=email.data).first()
        if email1 or email2:
            raise ValidationError('email is taken, please choose another one')
    def validate_ssn(self, ssn):
        try:
            x = int(ssn)
        except:
            raise ValidationError('SSN must be a number')
        if not len(ssn) == 14:
            raise ValidationError('SSN must be a 14 digit number')

class DoctorRegistrationForm(RegistrationForm):
    salary = IntegerField("Salary",  validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired(), Length(min=1, max=30)])
    hiring_date = DateField('Hiring date')



    

class PatientRegistrationForm(RegistrationForm):
    Condition= StringField('Condition')