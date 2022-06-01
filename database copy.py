from emergencydebartment import db
from emergencydebartment.models import Doctor, Patient, User , Report, Images
from flask_bcrypt import Bcrypt

#####!!!!!!!!!!!! this file only to test the database models !!!!!!!!!!!!!!!!!!!!!

bcrypt = Bcrypt()
db.drop_all()

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
patient1 = Patient(ssn=33141224008845, Fname='beko', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient2 = Patient(ssn=33441204008845, Fname='beeeko', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient3 = Patient(ssn=33141204608845, Fname='beeeeeeeko', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient4 = Patient(ssn=33141204098845, Fname='ali', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient5 = Patient(ssn=33141209098895, Fname='sameer', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient6 = Patient(ssn=33141208098845, Fname='5awl', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient7 = Patient(ssn=45141224008845, Fname='beko', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient8 = Patient(ssn=23441204008845, Fname='beeeko', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient9 = Patient(ssn=21141204608845, Fname='beeeeeeeko', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient10 = Patient(ssn=11141204098845, Fname='ali', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient11 = Patient(ssn=33141209098845, Fname='sameer', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
patient12 = Patient(ssn=33141208098245, Fname='5awl', Lname='mohamed', gender='male', user_role='Patient', password=hashed)
report1 = Report(patient_id= 3,doctor_id = 1, statement= "he will die soon")
report2 = Report(patient_id= 3,doctor_id = 2, statement= "al23mar bed allah")
image1 = Images(image="image1.jpg", report_id=1)
image2 = Images(image="image2.jpg", report_id=2)
image3 = Images(image="image1.jpg", report_id=1)
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

db.session.add(report1) 
db.session.add(report2) 
db.session.add(image1)
db.session.add(image2)
db.session.add(image3) 
db.session.commit()