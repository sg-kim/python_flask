from flask import Flask
from DBwithFlaskPackage.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '08e72ef1b6c5200e2093c9250b945109'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from DBwithFlaskPackage import routes

