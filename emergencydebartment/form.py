
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, EmailField,IntegerField,DateField, RadioField, MultipleFileField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from emergencydebartment.models import Doctor, Patient
import re   
  
 







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
    email = StringField('Email', validators=[ ])
    birth_date = DateField('BirthDate')
    gender = RadioField(choices=["Male","Female"])
    address = StringField('Home address', validators=[DataRequired(), Length(min=1, max=30)])
    phone = StringField('Phone number')
    password = PasswordField('Password', validators=[ Length(min=0, max=30)])
    confirm_password = PasswordField('Confirm password',validators=[EqualTo('password')])
    submit = SubmitField('sign up')
    def validate_email(self, email):
        if email.data:
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            
            if not (re.fullmatch(regex,email.data)):   
                raise ValidationError('email is invalid, please enter a valid email')
            email1 =  Doctor.query.filter_by(email=email.data).first()
            email2 =  Patient.query.filter_by(email=email.data).first()
            if email1 or email2:
                raise ValidationError('email is taken, please choose another one')
    def validate_phone(self, phone):
        print (phone.data)
        if phone.data:
            try:
                x = int(phone.data)
                if not len(phone.data) == 11 :
                    raise ValidationError('phone number is invalid')
                    
                if phone.data[0] != '0' or phone.data[1] != '1':
                    raise ValidationError('phone number is invalid')
            except:
                raise ValidationError('phone number is invalid')
        
    def validate_ssn(self, ssn):
        try:
            x = int(ssn.data)
            if not (len(ssn.data) == 14):
                
                raise ValidationError('SSN must be a 14 digit number')
        except ValueError:
            
            raise ValidationError('SSN must be a 14 digit number')
        user1 = Doctor.query.filter_by(ssn = ssn.data).first()
        user2 = Patient.query.filter_by(ssn = ssn.data).first()
        if user1 or user2:
             raise ValidationError('This SSN is already registered')

class DoctorRegistrationForm(RegistrationForm):
    
    salary = IntegerField("Salary",  validators=[DataRequired()])
    speciality = StringField('Department', validators=[DataRequired(), Length(min=1, max=30)])
   
class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=1, max=30)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=1, max=30)])
    confirm_new_password = PasswordField('Confirm New Password',validators=[EqualTo('new_password')])
    submit = SubmitField('Change password')

    

class PatientRegistrationForm(RegistrationForm):
    Condition= StringField('Condition')

class ReportForm(FlaskForm):
    ssn = StringField('Patient SSN')
    title = StringField('Basic condition', validators=[DataRequired()])
    condition = TextAreaField('Condition', validators=[DataRequired()])
    urgency = RadioField('Urgency level', choices=["Level 1","Level 2", "Level 3", "Level 4"])
    treatment = TextAreaField('Treatment given')
    recommendation = TextAreaField('Recommendation')
    images = MultipleFileField('Upload Files')
    submit = SubmitField('Add report')

    def validate_ssn(self, ssn):
        if ssn.data:
            try:
                x = int(ssn.data)
                print(len(str(ssn.data)))
                if len(str(ssn.data)) != 14:
                    raise ValidationError('SSN must be a 14 digit number')
            except ValueError:
                raise ValidationError('SSN must be a 14 digit number')
