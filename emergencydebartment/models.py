import email
from email.policy import default
from emergencydebartment import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(db.Model, UserMixin):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.Integer, unique=True,nullable=False)
    Fname = db.Column(db.String(20),nullable=False)
    Sname = db.Column(db.String(20))
    Lname = db.Column(db.String(20),nullable=False)
    gender = db.Column(db.String(6),nullable=False)
    phone = db.Column(db.String(11), default='Unknown')
    address = db.Column(db.String(70), default='Unknown')
    birth_date = db.Column(db.DateTime)
    user_role = db.Column(db.String(15), nullable=False, default='Patient') 
    password = db.Column(db.String(61),nullable=False)

    def __repr__(self):
        return f"User('{self.email}','{self.user_role}')"
    

class Doctor(User):
    id = db.Column(db.Integer, db.ForeignKey('user_table.id'),primary_key=True)
    hiring_date = db.Column(db.DateTime, nullable=False,default = datetime.utcnow)
    salary = db.Column(db.Integer, nullable=False)
    speciallity = db.Column(db.String(80))
    image_file = db.Column(db.String(20),nullable = False, default='default.jpg')
    email = db.Column(db.String(20),unique=True,nullable=False)
    examination = db.relationship('Report',  backref='doctor', lazy=True, foreign_keys = 'Report.doctor_id')
    def __repr__(self):
        return f"Doctor('{self.Fname}','{self.Lname}')"

class Patient(User):
    id = db.Column(db.Integer, db.ForeignKey('user_table.id'),primary_key=True)
    report = db.relationship('Report',  backref='patient', lazy=True, foreign_keys = 'Report.patient_id')
    
    email = db.Column(db.String(20),unique=True,nullable=False, default = 'patient@hospital.com')
    
    
    def __repr__(self):
        return f"Patient('{self.Fname}','{self.Lname}')"

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'),nullable = False, default='Unknown Patient')
    doctor_id =  db.Column(db.Integer, db.ForeignKey('doctor.id'),nullable = False)
    date =  db.Column(db.DateTime, default = datetime.utcnow)
    statement = db.Column(db.String(300))
    images = db.relationship('Images',  backref='Report', lazy=True, foreign_keys = 'Images.report_id')
    
    def __repr__(self):
        return f"Report('{self.statement}')"

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20),nullable = False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'),nullable = False)
    def __repr__(self):

        return f"image('{self.image}')"