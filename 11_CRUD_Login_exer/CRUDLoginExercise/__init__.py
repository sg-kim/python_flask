from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '4e21c40eed22ff2c79a3546482a8e321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://engineer:'DB password'@localhost/CRUD_Login_db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'info'

from CRUDLoginExercise import routes

