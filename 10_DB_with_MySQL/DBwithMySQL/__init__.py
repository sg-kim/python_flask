from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://engineer:heybuddy01@localhost:3306/flask_test_db'
db = SQLAlchemy(app)

