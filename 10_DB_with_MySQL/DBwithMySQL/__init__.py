from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://engineer:heybuddy01@localhost:3306/flask_test_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://engineer:heybuddy01@localhost/flask_test_db'
db = SQLAlchemy(app)

