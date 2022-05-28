from emergencydebartment import db
from emergencydebartment.models import Doctor, Patient, User
from flask_bcrypt import Bcrypt

#####!!!!!!!!!!!! this file only to test the database models !!!!!!!!!!!!!!!!!!!!!

bcrypt = Bcrypt()
db.create_all()

hashed = bcrypt.generate_password_hash('admin').decode('utf-8')
doctor = Doctor(email='admin@admin.com',ssn=30112040088445, Fname='ahmed', Lname='mohamed', gender='male', user_role='Admin', password=hashed, salary=1000000)

db.session.add(doctor) 
db.session.commit()

hashed = bcrypt.generate_password_hash('doctor').decode('utf-8')
doctor = Doctor(email='doctor@doctor.com',ssn=32112040088445, Fname='D.maahas', Lname='mohamed', gender='male', user_role='Doctor', password=hashed, salary=1000000)

db.session.add(doctor) 
db.session.commit()

hashed = bcrypt.generate_password_hash('patient').decode('utf-8')
patient = Patient(email='patient@patient.com',ssn=33141204008845, Fname='amr', Lname='mohamed', gender='male', user_role='Patient', password=hashed, doctor_id = 1)

db.session.add(patient) 
db.session.commit()