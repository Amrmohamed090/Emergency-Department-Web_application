from turtle import title
from emergencydebartment import db
from emergencydebartment.models import Doctor, Patient, User , Report, Images
from flask_bcrypt import Bcrypt
from datetime import datetime

#####!!!!!!!!!!!! this file only to test the database models !!!!!!!!!!!!!!!!!!!!!

bcrypt = Bcrypt()
db.drop_all()

db.create_all()

#admin password = admin
# admin email endup with @admin.com


#email:house@doctor.com
#pass:doctor
password_hashed = bcrypt.generate_password_hash('admin').decode('utf-8')
doctor = Doctor(email='admin@admin.com',ssn=30112040088445, Fname='Ahmed', Sname='Mohamed',Lname='Ahmed', gender='Male', user_role='Admin',birth_date=datetime(1990,12,10),password=password_hashed, salary=1000000, address="Giza hadayk alahram 185 street 12",speciallity="Dentist",  phone='01123457364')

db.session.add(doctor) 
db.session.commit()

#doctor password = doctor
# doctor email endup with @doctor.com
password_hashed = bcrypt.generate_password_hash('doctor').decode('utf-8')
doctor = Doctor(email='house@doctor.com',ssn=30152040088445, Fname='Gregory', Sname='Hugh',Lname='House', gender='Male', user_role='Doctor', speciallity='Diagnostic Medicine',birth_date=datetime(1973,12,10),password=password_hashed, salary=1000, address="221 B Baker street",  phone='01223847254')

db.session.add(doctor) 
db.session.commit()

#patient password is 'patient'
#but default in the app is the ssn of the patient
# patient email endup with @hospital
password_hashed = bcrypt.generate_password_hash('patient').decode('utf-8')

#password:  patient
patient = Patient(ssn=30251204008845,email='amr8845@hospital.com', Fname='amr',Sname="", Lname='mohamed', gender='male', birth_date=datetime(1999,10,12),password=password_hashed, phone='01023847364')
patient1 = Patient(ssn=30141224008845,email='eslam8845@hospital.com', Fname='eslam',Sname="", Lname='ibrahim', gender='male', birth_date=datetime(1993,11,10),password=password_hashed, phone='01023847364' )
patient2 = Patient(ssn=30441204008845,email='reda8845@hospital.com', Fname='reda',Sname="ibrahim", Lname='mohamed', gender='male', birth_date=datetime(1934,2,10),password=password_hashed, phone='01023347364')
patient3 = Patient(ssn=30141204608845,email='sara8845@hospital.com', Fname='sara',Sname="ahmed", Lname='mohamed', gender='Female', birth_date=datetime(1990,3,10),password=password_hashed, phone='01023447364')
patient4 = Patient(ssn=30141204098845,email='ali8845@hospital.com', Fname='ali', Sname="tawfiq", Lname='mohamed', gender='male', birth_date=datetime(1980,4,10),password=password_hashed, phone='01023845364')
patient5 = Patient(ssn=30141209098895,email='sameer8895@hospital.com', Fname='sameer', Sname="", Lname='mohamed', gender='male', birth_date=datetime(1970,5,10),password=password_hashed, phone='01023846364')
patient6 = Patient(ssn=30141208098845,email='sondos8845@hospital.com', Fname='sondos', Sname="mamdoh", Lname='abd alrahman', gender='Female', birth_date=datetime(1999,7,12),password=password_hashed, phone='01223847364')
patient7 = Patient(ssn=29141224008845,email='yousef8845@hospital.com', Fname='yousef', Sname="ahmed", Lname='khaled', gender='male', birth_date=datetime(2000,10,13),password=password_hashed, phone='01123847364')
patient8 = Patient(ssn=29441204008845,email='seif8845@hospital.com', Fname='seif', Sname="soraika", Lname='shekabala', gender='male', birth_date=datetime(1992,1,12),password=password_hashed, phone='01223847364')
patient9 = Patient(ssn=30141904668845,email='abdelmenem8845@hospital.com', Fname='abdelmenem', Sname="ryad", Lname='fatoh', gender='male', birth_date=datetime(1994,1,12),password=password_hashed, phone='01323847364')
patient10 = Patient(ssn=30141704018245,email='ali8245@hospital.com', Fname='ali', Sname="gaber", Lname='khaled', gender='male', birth_date=datetime(1988,2,12),password=password_hashed, phone='01423847364')
patient11 = Patient(ssn=30141509098845,email='momen8845@hospital.com', Fname='momen', Sname="ahmed", Lname='mohamed', gender='male', birth_date=datetime(1989,12,11),password=password_hashed, phone='01123847364')
patient12 = Patient(ssn=30141308098245,email='zyad8245@hospital.com', Fname='zyad', Sname="fathy", Lname='osama', gender='male', birth_date=datetime(1954,12,10),password=password_hashed, phone='01023347364')
db.session.add(patient)
db.session.add(patient1)
db.session.add(patient2)
db.session.add(patient3) 
db.session.add(patient4)
db.session.add(patient5)
db.session.add(patient6)
db.session.add(patient7) 
db.session.add(patient8)
db.session.add(patient9)
db.session.add(patient10)
db.session.add(patient11) 
db.session.add(patient12)
db.session.commit()
report1 = Report(patient_id= 3,doctor_id = 1,title= "myocardial infarction" ,condition= "The patient is a 20-year-old male who states that he has had two previous myocardial infarctions related to his use of amphetamines"
                                                                                                "The patient has not used amphetamines for at least four to five months, according to the patient; however, he had onset of chest pain this evening.The patient describes the pain as midsternal pain, a burning type sensation that lasted several seconds.        ", treatment= "nitroglycerin p.r.n.",recommendation="1. Evaluation of chest pain. 2. Possible esophageal reflux.",urgency= "level 2")
db.session.add(report1) 

 
db.session.commit()