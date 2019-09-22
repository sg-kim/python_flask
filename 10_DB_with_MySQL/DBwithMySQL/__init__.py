from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://engineer:'DB password'@localhost/flask_test_db'
db = SQLAlchemy(app)

