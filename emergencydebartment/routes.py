
from flask import  render_template, request, url_for ,flash, redirect, session
from emergencydebartment import app, db, bcrypt, login_manager
from emergencydebartment.form import LoginForm , DoctorRegistrationForm, PatientRegistrationForm
from emergencydebartment.models import Doctor, Patient
from flask_login import login_user, current_user , logout_user, login_required
from functools import wraps


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
              return login_manager.unauthorized()
            if ((current_user.user_role != role) and (role != "ANY")):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')



@app.route("/register-D", methods=['GET', 'POST'])
@login_required(role='Admin')
def registerD():
    form =  DoctorRegistrationForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        doctor = Doctor(Fname=form.Fname.data, Sname=form.Sname.data,Lname=form.Lname.data
                        ,email=form.email.data,ssn = form.ssn.data, password=hashed_password, gender=form.gender.data,
                        salary=form.salary.data, birth_date=form.birth_date.data,
                        address=form.address.data, speciallity = form.speciality.data)
        db.session.add(doctor)
        db.session.commit()
        flash('a doctor has been registered', 'successus')
        return redirect(url_for('home'))
    
    if form.errors:
        flash('please inter valid fields', 'danger')
        return redirect(url_for('registerD'))
    return render_template('signup-doctor.html', form=form)

@app.route("/register-P", methods=['GET', 'POST'])
@login_required(role='Doctor')
def registerP():
    form =  PatientRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password).decode('utf-8')
        patient = Patient(Fname=form.Fname.data, Sname=form.Sname.data,Lname=form.Lname.data
                        ,email=form.email.data,ssn = form.ssn.data, password=hashed_password, gender=form.gender.data,
                         birth_date=form.birth_date.data,
                        address=form.address.data)
        print('done')
        flash('a Patient has been registered', 'successus')
        return redirect(url_for('home'))
        
        
    return render_template('signup-patient.html', form=form)






@app.route("/login",methods=['GET','POST'])
def login():
    print(type(current_user._get_current_object()).__name__)
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Doctor.query.filter_by(email=form.email.data).first()
        print (user)
        if not user:
            user = Patient.query.filter_by(email=form.email.data).first()
            print (user)
        
            
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        
        else:
            flash('Please check your username and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))