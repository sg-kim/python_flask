from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://quanto:heybuddy01@localhost/flask_study'

db = SQLAlchemy(app)

engine = create_engine('mysql+pymysql://quanto:heybuddy01@localhost/flask_study')

