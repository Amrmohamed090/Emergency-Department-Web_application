
from turtle import title
from flask import  render_template, request, url_for ,flash, redirect, session
from emergencydebartment import app, db, bcrypt, login_manager
from emergencydebartment.form import LoginForm , DoctorRegistrationForm, PatientRegistrationForm, ReportForm, SearchPatientForm
from emergencydebartment.models import Doctor, Patient, Report, Images
from flask_login import login_user, current_user , logout_user, login_required
from functools import wraps
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



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
    return render_template('signup-doctor.html', form=form , title = "Register a Doctor")

@app.route("/register-P", methods=['GET', 'POST'])
@login_required(role='Doctor')
def registerP():
    form =  PatientRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        patient = Patient(Fname=form.Fname.data, Sname=form.Sname.data,Lname=form.Lname.data
                        ,email=form.email.data,ssn = form.ssn.data, password=hashed_password, gender=form.gender.data,
                         birth_date=form.birth_date.data,phone = form.phone.data,
                        address=form.address.data)
        db.session.add(patient)
        db.session.commit()
    
        flash('a Patient has been registered', 'successus')
        return redirect(url_for('home'))
    
        
        
    return render_template('signup-patient.html', form=form, title = "Register a Patient")


@app.route("/report/new", methods=['GET', 'POST'])
@login_required(role = 'Doctor')
def new_report():
    form = ReportForm()
    if form.validate_on_submit():
        

        
        files = form.images.data
        print(files)
        
        if files:
            for file in files:
                print(file)
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
                if file and not allowed_file(file.filename):
                    flash(f'Your file "{file.filename}" is not supported', 'danger')
                    return redirect(url_for('new_report'))
            
        
        
        patient = Patient.query.filter_by(ssn = form.ssn.data).first()
        ssn_exist = 1
        if not patient:
            report = Report(doctor_id=current_user.id,
                             statement = form.statement.data)
            db.session.add(report)
            db.session.commit()
            flash('Your Report has been created! ', 'success')
            return render_template('create_report.html', form=form, legend='Add report', title = "Add report" ,ssn_notexist = 1)
        else:
            report = Report(patient_id = patient.id, doctor_id=current_user.id,
                             statement = form.statement.data)
            db.session.add(report)
            db.session.commit()
            flash('Your Report has been created!', 'success')
            
            return render_template('create_report.html', form=form, legend='Add report', title = "Add report" )
        
    return render_template('create_report.html', form=form, legend='Add report', title = "Add report" )


@app.route("/search",methods=['GET','POST'])
def search_patient():
    form = SearchPatientForm()
    if form.validate_on_submit():
        pass
    return render_template('search_patient.html',form=form, title = "search")

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
    return render_template('login.html',form=form, title = "login")



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/patients_table")
def ptable():
    table = Patient.query.all()
    return render_template('patients_table.html', table = table)
