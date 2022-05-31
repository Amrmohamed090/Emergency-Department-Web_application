from emergencydebartment import db
from emergencydebartment.models import Doctor, Patient, User , Report, Images
from flask_bcrypt import Bcrypt

#####!!!!!!!!!!!! this file only to test the database models !!!!!!!!!!!!!!!!!!!!!

bcrypt = Bcrypt()
db.create_all()

hashed = bcrypt.generate_password_hash('admin').decode('utf-8')
doctor = Doctor(email='admin@admin.com',ssn=30112040088445, Fname='ahmed', Lname='mohamed', gender='Male', user_role='Admin', password=hashed, salary=1000000)

db.session.add(doctor) 
db.session.commit()

hashed = bcrypt.generate_password_hash('doctor').decode('utf-8')
doctor = Doctor(email='doctor@doctor.com',ssn=32112040088445, Fname='D.maahas', Lname='mohamed', gender='male', user_role='Doctor', password=hashed, salary=1000000)

db.session.add(doctor) 
db.session.commit()

hashed = bcrypt.generate_password_hash('patient').decode('utf-8')
patient = Patient(ssn=33141204008845, Fname='amr', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
report1 = Report(patient_id= 3,doctor_id = 1, statement= "he will die soon")
report2 = Report(patient_id= 3,doctor_id = 2, statement= "al23mar bed allah")
image1 = Images(image="image1.jpg", report_id=1)
image2 = Images(image="image2.jpg", report_id=2)
image3 = Images(image="image1.jpg", report_id=1)
db.session.add(patient) 
db.session.add(report1) 
db.session.add(report2) 
db.session.add(image1)
db.session.add(image2)
db.session.add(image3) 
db.session.commit()