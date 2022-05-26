
from flask import  render_template, request, url_for ,flash, redirect
from emergencydebartment import app, db, bcrypt
from emergencydebartment.form import LoginForm , RegistrationForm
from emergencydebartment.models import Admin, Doctor, Patient
from flask_login import login_user, current_user
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')



@app.route("/admin")
def admin():
    return render_template('admin-home.html')

@app.route("/register-D", methods=['GET', 'POST'])
def registerD():
    form =  RegistrationForm()
    if form.validate_on_submit():
        #hashed_password = bcrypt.generate_password_hash(form.password).decode('utf-8')
        #doctor = Doctor(Fname=form.Fname.data,Lname=form.Lname.data,Sname=form.Sname.data,email=form.email.data, pasword=hashed_password, gender=form.gender.data,salary=form.salary.data)
        print('done')
        flash('a doctor has been registered', 'successus')
        return redirect(url_for('admin'))
        
        
    return render_template('signup-doctor.html', form=form)





@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Doctor.query.filter_by(email=form.email.data).first()
        
        if not user:
            user= Patient.query.filter_by(email=form.email.data).first()
            
        if not user:
            user= Admin.query.filter_by(email=form.email.data).first()
            
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        
        else:
            flash('Please check your username and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html',form=form)

