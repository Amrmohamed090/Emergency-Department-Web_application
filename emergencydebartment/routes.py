
from turtle import title
from flask import  render_template, request, url_for ,flash, redirect, session, abort
import secrets
from emergencydebartment import app, db, bcrypt, login_manager
from emergencydebartment import form
from emergencydebartment.form import LoginForm , DoctorRegistrationForm, PatientRegistrationForm, ReportForm, ResetPasswordForm
from emergencydebartment.models import Doctor, Patient, Report, Images
from flask_login import login_user, current_user , logout_user, login_required
from functools import wraps
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#########################################
#LOGIN DECORATOR
def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
              return login_manager.unauthorized()
            if current_user.user_role != 'Admin':
                if ((current_user.user_role != role) and (role != "ANY")):
                    return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
##############################################
#HOME
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')
##############################################

#REGISTER DOCTOR
@app.route("/register-D", methods=['GET', 'POST'])
@login_required(role='Admin')
def registerD():
    form =  DoctorRegistrationForm()
    
    if form.validate_on_submit():
        print('heeere')
        #set defualt email and password if left empty
        if not form.email.data:
            form.email.data = form.Fname.data + str(form.ssn.data)[11:14]  + '@hospital.com'
        if not form.password.data:
            form.password.data = str(form.ssn.data)
        #encrypting password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #adding doctor to db
        doctor = Doctor(Fname=form.Fname.data, Sname=form.Sname.data,Lname=form.Lname.data
                        ,email=form.email.data,ssn = form.ssn.data, password=hashed_password, gender=form.gender.data,
                        salary=form.salary.data, birth_date=form.birth_date.data,
                        address=form.address.data, speciallity = form.speciality.data, user_role="Doctor")
        db.session.add(doctor)
        db.session.commit()
        flash('a doctor has been registered', 'success')
        return redirect(url_for('home'))
    return render_template('signup-doctor.html', form=form , title = "Register a Doctor")
##############################################
#REGISTER PATIENT
@app.route("/register-P", methods=['GET', 'POST'])
@login_required(role='Doctor')
def registerP():
    form =  PatientRegistrationForm()
    if form.validate_on_submit():
        if not form.email.data:
            form.email.data = form.Fname.data + str(form.ssn.data)[11:14]  + '@hospital.com'
        if not form.password.data:
            form.password.data = str(form.ssn.data)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        patient = Patient(Fname=form.Fname.data, Sname=form.Sname.data,Lname=form.Lname.data
                        ,email=form.email.data,ssn = form.ssn.data, password=hashed_password, gender=form.gender.data,
                         birth_date=form.birth_date.data,phone = form.phone.data,
                        address=form.address.data)
        
        db.session.add(patient)
        db.session.commit()
        patient = Patient.query.filter_by(ssn = form.ssn.data).first()
        print(patient)
        reports = Report.query.filter_by(patient_ssn = form.ssn.data).all()
        print(reports)
        if reports:
            for report in reports:
                report.patient_id = patient.id
                report.patient_ssn = patient.ssn
                db.session.commit()
            flash('a Patient has been registered, there is ' + str(len(reports)) + ' medical reports has been registered with this patient SSN', 'success')
            return redirect(url_for('home'))
    
        flash('a Patient has been registered', 'success')
        return redirect(url_for('home'))
    return render_template('signup-patient.html', form=form, title = "Register a Patient")
##############################################
#REGISTER PATIENTS WITH AUTO FILL FOR SSN
@app.route("/register-P/<int:ssn>", methods=['GET', 'POST'])
@login_required(role='Doctor')
def registerP_withssn(ssn):
    form =  PatientRegistrationForm()
    if form.validate_on_submit():
        if not form.email.data:
            form.email.data = form.Fname.data + str(form.ssn.data)[11:14]  + '@hospital.com'
        if not form.password.data:
            form.password.data = str(form.ssn.data)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        patient = Patient(Fname=form.Fname.data, Sname=form.Sname.data,Lname=form.Lname.data
                        ,email=form.email.data,ssn = form.ssn.data, password=hashed_password, gender=form.gender.data,
                         birth_date=form.birth_date.data,phone = form.phone.data,
                        address=form.address.data)
        
        db.session.add(patient)
        db.session.commit()
        patient = Patient.query.filter_by(ssn = form.ssn.data).first()
        print(patient)
        reports = Report.query.filter_by(patient_ssn = form.ssn.data).all()
        print(reports)
        if reports:
            for report in reports:
                report.patient_id = patient.id
                report.patient_ssn = patient.ssn
                db.session.commit()
            flash('a Patient has been registered, there is ' + str(len(reports)) + 'medical reports has been registered with this patient SSN', 'success')
            return redirect(url_for('home'))
        flash('a Patient has been registered', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.ssn.data = ssn
    
        
    return render_template('signup-patient.html', form=form, title = "Register a Patient")
##############################################
#CREATE NEW REPORT
@app.route("/report/new", methods=['GET', 'POST'])
@login_required(role = 'Doctor')
def new_report():
    form = ReportForm()
    if form.validate_on_submit():
        
        files = form.images.data
        print(files)
        
        if files:
            images_names_list = list()
            for file in files:
                
                if file and not allowed_file(file.filename):
                    flash(f'Your file "{file.filename}" is not supported', 'danger')
                    return redirect(url_for('new_report'))
            
            for file in files:
                if file and allowed_file(file.filename):
                    
                    filename = secure_filename(file.filename)
                    _, f_ext = os.path.splitext(filename)
                    random_hex = secrets.token_hex(8)
                    picture_fn = random_hex + f_ext
                    file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], picture_fn))
                    images_names_list.append(picture_fn)
                
        
        if form.ssn.data:#doctor added ssn to report
            patient = Patient.query.filter_by(ssn = form.ssn.data).first()
            if not patient: #1111the patient is not in database, but ssn is provided, Create report with ssn but without id becuase the patient dont exist
                report = Report(doctor_id=current_user.id, title = form.title.data, patient_ssn = form.ssn.data,
                                condition = form.condition.data, urgency = form.urgency.data, treatment = form.treatment.data, recommendation = form.recommendation.data)
                db.session.add(report)
                db.session.commit()
                for image_name in images_names_list:
                    image = Images(image = image_name, report_id = report.id)
                    db.session.add(image)
                    db.session.commit()
                flash('Your Report has been created! note that this patient is not registered yet, Do you want to register the patient now?', 'registernow')
                return render_template('create_report.html', form=form, legend='Add report', title = "Add report" )
            else: #222222patient is in the database,  Create report patient_id and ssn
                report = Report(patient_id=patient.id,doctor_id=current_user.id, title = form.title.data, patient_ssn = form.ssn.data,
                                condition = form.condition.data, urgency = form.urgency.data, treatment = form.treatment.data, recommendation = form.recommendation.data)
                db.session.add(report)
                db.session.commit()
                for image_name in images_names_list:
                    image = Images(image = image_name, report_id = report.id)
                    db.session.add(image)
                    db.session.commit()
                flash('Your Report has been created', 'success')
                return render_template('create_report.html', form=form, legend='Add report', title = "Add report" )


        else: #333333333doctor didnt add ssn to report, Create report with no patient_id or ssn, the ssn will be set to anonymous
            report = Report( doctor_id=current_user.id,
                              title = form.title.data, condition = form.condition.data, urgency = form.urgency.data, treatment = form.treatment.data, recommendation = form.recommendation.data)
            db.session.add(report)
            db.session.commit()
            for image_name in images_names_list:
                    image = Images(image = image_name, report_id = report.id)
                    db.session.add(image)
                    db.session.commit()
            flash('Your Report has been created! You did not provide ssn for the patient, please update the report to provide an ssn as soon as possible', 'success')
            return render_template('create_report.html', form=form, legend='Add report', title = "Add report" )
        
    return render_template('create_report.html', form=form, legend='Add report', title = "Add report" )
#####################################################

##############################################
#SEARCH FOR A PATIENT
@app.route("/search_patient",methods=['GET','POST'])
@login_required(role = 'Doctor')
def search_patient_main():
    if request.method == 'POST':
    
        try:
            ssn= int(request.form.get('search'))
        except ValueError:
            flash('please enter a valid ssn', 'danger')
            return redirect(url_for('search_patient_main'))
        if len(request.form.get('search')) != 14:
            flash('please enter a valid ssn', 'danger')
            return redirect(url_for('search_patient_main'))
        else:
            patient = Patient.query.filter_by(ssn = ssn).first()
            
            if not patient:
                flash('This SSN doen not exist', 'danger')
                return redirect(url_for('search_patient_main'))
            else:
                print(patient)
                patient_ssn =  patient.ssn
                return redirect(url_for('search_patient', patient_ssn=patient_ssn))
    
    return render_template('search_patient.html', title = "search")
##############################################
#SEARCH RESULT AND SEARCH AGAIN IF YOU WANT
@app.route("/search_patient/<int:patient_ssn>",methods=['GET','POST'])
@login_required(role = 'Doctor')
def search_patient(patient_ssn):

    if request.method == 'POST':
    
        try:
            ssn= int(request.form.get('search'))
        except ValueError:
            name_list = request.form.get('search').split()
            return redirect(url_for('search_patient', patient_ssn=patient_ssn))
        if len(request.form.get('search')) != 14:
            flash('please enter a valid ssn', 'danger')
            return redirect(url_for('search_patient', patient_ssn=patient_ssn))
        else:
            patient = Patient.query.filter_by(ssn = ssn).first()
            
            if not patient:
                flash('This SSN doen not exist', 'danger')
                return redirect(url_for('search_patient', patient_ssn=patient_ssn))
            else:
                patient_ssn = patient.ssn
                return redirect(url_for('search_patient', patient_ssn=patient_ssn))
    reports = Report.query.filter_by(patient_ssn = patient_ssn)
    doctors_list = list()
    for report in reports:
        doctors_list.append(Doctor.query.get(report.doctor_id))

    final_patient = Patient.query.filter_by(ssn=patient_ssn).first()
    
    return render_template('search_patient.html', title = "search", patient = final_patient, report_doctor_list = list(zip(reports, doctors_list)))
##############################################

@app.route("/login",methods=['GET','POST'])
def login():
    print(type(current_user._get_current_object()).__name__)
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Doctor.query.filter_by(email=form.email.data).first()
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
##############################################
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
##############################################
@app.route("/resetpassword", methods= ['GET','POST'])
@login_required(role = 'ANY')
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if  bcrypt.check_password_hash(current_user.password, form.old_password.data):
            hashed = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password = hashed
            db.session.commit()
            flash('your password has been changed','success')
            return redirect(url_for('home'))
    return render_template('reset_password.html', form=form)


#######################################
#TABLE OF PATIENTS
@app.route("/patients_table", methods= ['GET','POST'])
@login_required(role = 'Doctor')
def ptable():
    
    table = Patient.query.all()
    num_of_reports = list()
    for patient in table:
        num_of_reports.append(len(patient.report))
    if request.method == 'POST':
    
        try:
            ssn= int(request.form.get('search'))
        except ValueError:
            flash('please enter a valid ssn', 'danger')
            return redirect(url_for('ptable'))
        if len(request.form.get('search')) != 14:
            flash('please enter a valid ssn', 'danger')
            return redirect(url_for('ptable'))
        else:
            return redirect(url_for('search_patient', patient_ssn=ssn))
    return render_template('patients_table.html', table = zip(table, num_of_reports))
    #######################################
    #TABLE OF DOCTORS
@app.route("/doctors_table", methods= ['GET','POST'])
@login_required(role = 'Admin')
def dtable():
    
    table = Doctor.query.all()
    num_of_reports = list()
    for doctor in table:
        num_of_reports.append(len(doctor.examination))
    
    return render_template('doctor_table.html', table = zip(table, num_of_reports))
##############################################
#REPORT PAGE
@app.route("/report/<int:report_id>")
@login_required(role = 'ANY')
def report(report_id):
    report = Report.query.get_or_404(report_id)
    patient = Patient.query.get(report.patient_id)
    if current_user.user_role == "Patient" and current_user.id != patient.id:
        abort(403)

    doctor = Doctor.query.get(report.doctor_id)
    
    images = report.images
    return render_template('patient_report.html', report = report, doctor=doctor, patient=patient, images=images)
##############################################
#PROFILE OF A DOCTOR
@app.route("/profile/<int:doctor_id>")
@login_required(role = 'Doctor')
def profile(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    reports = doctor.examination
    patients_names_list = list()
   
    for report in reports:
        if report.patient_id != 99999999999999:patients_names_list.append(Patient.query.get(report.patient_id).Fname + " "+Patient.query.get(report.patient_id).Lname )
        else:patients_names_list.append('unkown patient')

    print(patients_names_list)
    
    return render_template('profile.html', doctor= doctor, reports_names= list(zip(reports, patients_names_list)))
##############################################
#PROFILE OF A patient
@app.route("/profile_patient/<int:patient_id>")
@login_required(role = 'ANY')

def profile_patient(patient_id):
    if current_user.user_role == "Patient" and current_user.id != patient_id:
       abort(403)
    patient = Patient.query.get_or_404(patient_id)
    reports = patient.report
    doctors_names_list = list()
   
    for report in reports:
       doctors_names_list.append(Doctor.query.get(report.doctor_id).Fname + " " + Doctor.query.get(report.doctor_id).Lname)

    print(doctors_names_list)
    
    return render_template('profile_patient.html', patient= patient, reports_names= list(zip(reports, doctors_names_list)))
##############################################


#Update report
@app.route("/report_update/<int:report_id>", methods=['GET', 'POST'])
@login_required(role = 'Doctor')
def update_report(report_id):
    report = Report.query.get_or_404(report_id)
    if current_user.id != report.doctor_id:
        abort(403)
    form = ReportForm()

    if request.method == "GET":

        if report.patient_ssn != 99999999999999:
            form.ssn.data = report.patient_ssn
        
        
        form.title.data = report.title
        form.condition.data = report.condition
        form.urgency.data = report.urgency
        form.treatment.data = report.treatment
        form.recommendation.data = report.recommendation


    if form.validate_on_submit():
        report.recommendation = form.recommendation.data
        report.treatment = form.treatment.data
        report.urgency = form.urgency.data
        report.condition = form.condition.data
        report.title = form.title.data
        print('11')
        if form.ssn.data != report.patient_ssn: #doctor updated ssn
            print('22')
            patient = Patient.query.filter_by(ssn = form.ssn.data).first()
            if patient: #doctor updated ssn to an existing patient
                print('33')
                report.patient_id = patient.id
                report.patient_ssn = patient.ssn
                db.session.commit()
                flash("Report has been updated successfully, note that the report has been set to" + patient.Fname + " " + patient.Lname + "with ssn" + patient.ssn, "success")
                return redirect(url_for("update_report", report_id = report_id))
            else: #doctor updated ssn to a NON existing patient
                print('44')
                report.patient_ssn = form.ssn.data
                db.session.commit()
                flash("Report has been updated successfully, note that you have set the patient is not registered, do you want to register the patient now?", 'registernow')
                return redirect(url_for("update_report", report_id = report_id))
        else: #doctor didnt update ssn
            print('55')
            db.session.commit()
            flash("Report has been updated successfully", "success")
            return redirect(url_for("update_report", report_id = report_id))

    return render_template('update_report.html', form=form, legend='Update report', title = "Update report" )

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")