from turtle import title
from emergencydebartment import db
from emergencydebartment.models import Doctor, Patient, User , Report, Images
from flask_bcrypt import Bcrypt
from datetime import datetime

#####!!!!!!!!!!!! this file only to test the database models !!!!!!!!!!!!!!!!!!!!!

bcrypt = Bcrypt()
db.drop_all()

db.create_all()

hashed = bcrypt.generate_password_hash('admin').decode('utf-8')
doctor = Doctor(email='admin@admin.com',ssn=30112040088445, Fname='ahmed', Lname='mohamed', gender='Male', user_role='Admin', speciallity='Emergency',birth_date=datetime(1990,10,10),password=hashed, salary=1000000)

db.session.add(doctor) 
db.session.commit()

hashed = bcrypt.generate_password_hash('doctor').decode('utf-8')
doctor = Doctor(email='doctor@doctor.com',ssn=32112040088445, Fname='maahas', Lname='mohamed', gender='male', user_role='Doctor', birth_date=datetime(1990,10,10),password=hashed, speciallity='oncology' ,salary=1000000)

db.session.add(doctor) 
db.session.commit()

hashed = bcrypt.generate_password_hash('patient').decode('utf-8')
patient = Patient(ssn=33141204008845, Fname='amr', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,10),password=hashed)
patient1 = Patient(ssn=33141224008845, Fname='beko', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,10),password=hashed)
patient2 = Patient(ssn=33441204008845, Fname='beeeko', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,10),password=hashed)
patient3 = Patient(ssn=33141204608845, Fname='beeeeeeeko', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,10),password=hashed)
patient4 = Patient(ssn=33141204098845, Fname='ali', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1980,10,10),password=hashed)
patient5 = Patient(ssn=33141209098895, Fname='sameer', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1970,11,10),password=hashed)
patient6 = Patient(ssn=33141208098845, Fname='5awl', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1999,10,12),password=hashed)
patient7 = Patient(ssn=45141224008845, Fname='beko', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(2000,10,13),password=hashed)
patient8 = Patient(ssn=23441204008845, Fname='beeeko', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,14),password=hashed)
patient9 = Patient(ssn=21141204608845, Fname='beeeeeeeko', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,15),password=hashed)
patient10 = Patient(ssn=11141204098845, Fname='ali', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,16),password=hashed)
patient11 = Patient(ssn=33141209098845, Fname='sameer', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,10,11),password=hashed)
patient12 = Patient(ssn=33141208098245, Fname='5awl', Lname='mohamed', gender='male', user_role='Patient', birth_date=datetime(1990,12,10),password=hashed)
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
report1 = Report(patient_id= 3,doctor_id = 1,title= "titlekosomk" ,condition= "213126534643567345he will die soon", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 1")
report2 = Report(patient_id= 3,doctor_id = 2,title='titlekosomen1231 omk' ,condition= "3213al23mar bed allah", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 1")
report3 = Report(patient_id= 3,doctor_id = 1,title= "titlekosom231k" ,condition= "123312he will die soon", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 3")
report4 = Report(patient_id= 3,doctor_id = 2,title='titlekosom35en omk' ,condition= "12374al23mar bed allah", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 1")
report5 = Report(patient_id= 3,doctor_id = 1,title= "titlekos546omk" ,condition= "678679078he will die soon", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 4")
report6 = Report(patient_id= 3,doctor_id = 2,title='titlekos456omen omk' ,condition= "678677al23mar bed allah", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 2")
report7 = Report(patient_id= 3,doctor_id = 1,title= "titleko546somk" ,condition= "6786897978he will die soon", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 1")
report8 = Report(patient_id= 3,doctor_id = 2,title='titlekos745omen omk' ,condition= "67867al23mar bed allah", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 3")
report9 = Report(patient_id= 3,doctor_id = 1,title= "titleko867somk" ,condition= "67823423467he will die soon", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 2")
report0 = Report(patient_id= 3,doctor_id = 2,title='titlekos768678omen omk' ,condition= "678678al23mar bed allah", treatment= "treatment treatment treatment treatment",recommendation="recommendationrecommendation",urgency= "level 1")

db.session.add(report1) 
db.session.add(report2) 
db.session.add(report3)
db.session.add(report4)
db.session.add(report5)
db.session.add(report6) 
db.session.add(report7)
db.session.add(report8)
db.session.add(report9)
db.session.add(report0) 

 
db.session.commit()