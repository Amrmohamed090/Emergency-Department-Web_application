from emergencydebartment import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(db.Model, UserMixin):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20),unique=True,nullable=False)
    Fname = db.Column(db.String(20),nullable=False)
    Sname = db.Column(db.String(20))
    Lname = db.Column(db.String(20),nullable=False)
    gender = db.Column(db.String(6),nullable=False)
    birth_date = db.Column(db.DateTime)
    user_role = db.Column(db.String(15), nullable=False, default='Patient') 
    phone = db.Column(db.String(11), default='Unknown')
    image_file = db.Column(db.String(20),nullable = False, default='default.jpg')
    address = db.Column(db.String(70), default='Unknown')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.email}','{self.user_role}')"
    

class Doctor(User):
    id = db.Column(db.Integer, db.ForeignKey('user_table.id'),primary_key=True)
    hiring_date = db.Column(db.DateTime, nullable=False,default = datetime.utcnow)
    salary = db.Column(db.Integer, nullable=False)
    speciallity = db.Column(db.String(80))
    examination = db.relationship('Patient',  backref='doctor', lazy=True, foreign_keys = 'Patient.doctor_id')
    
    def __repr__(self):
        return f"Doctor('{self.Fname}','{self.Lname}')"

class Patient(User):
    id = db.Column(db.Integer, db.ForeignKey('user_table.id'),primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'),nullable = False)
    
    def __repr__(self):
        return f"Patient('{self.Fname}','{self.Lname}')"
