from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '4e21c40eed22ff2c79a3546482a8e321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://engineer:heybuddy01@localhost/CRUD_Login_db'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db = SQLAlchemy(app)

from CRUDLoginExercise import routes

