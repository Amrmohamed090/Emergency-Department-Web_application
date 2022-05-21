# kosom aktb de b3d kda 
from flask import Flask
# kosom aktb de b3d kda 
from enum import unique
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '605c89ab0256f331e0a1b2ec2f08c646'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



from emergencydebartment import routes
