from emergencydebartment import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_admin(user_id):
    return Admin.query.get(int(user_id))

@login_manager.user_loader
def load_doctor(user_id):
    return Doctor.query.get(int(user_id))

@login_manager.user_loader
def load_patient(user_id):
    return Patient.query.get(int(user_id))

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable = False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    

    def __repr__(self):
        return f"Admin('{self.email}','{self.image_file}')"

class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Fname = db.Column(db.String(20),nullable=False)
    Sname = db.Column(db.String(20))
    Lname = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(30), nullable = False)
    power = db.Column(db.Boolean, default = False)
    gender = db.Column(db.String(6),nullable=False)
    hiring_date = db.Column(db.DateTime, nullable=False,default = datetime.utcnow)
    birth_date = db.Column(db.DateTime)
    salary = db.Column(db.Integer, nullable=False)
    speciallity = db.Column(db.String(80))
    examination = db.relationship('Patient', backref='doctor', lazy=True )
    
    def __repr__(self):
        return f"User('{self.Fname}','{self.Lname}')"


class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(30), nullable = False)
    Fname = db.Column(db.String(20),nullable=False)
    Sname = db.Column(db.String(20))
    Lname = db.Column(db.String(20),nullable=False)
    birth_date = db.Column(db.DateTime)
    address = db.Column(db.String(70))
    phone = db.Column(db.String(11))

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'),nullable = False)
    
    def __repr__(self):
        return f"User('{self.Fname}','{self.Lname}')"
