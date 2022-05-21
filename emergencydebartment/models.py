from emergencydebartment import db
from datetime import datetime



class Admin(db.Model):
    ssn = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable = False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True )

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"