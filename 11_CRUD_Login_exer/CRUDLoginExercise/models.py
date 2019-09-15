from datetime import datetime
from CRUDLoginExercise import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def	load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	email = db.Column(db.String(50), unique = True, nullable = False)
	password = db.Column(db.String(60), nullable = False)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String(20), unique = True, nullable = False)
	title = db.Column(db.String(50), nullable = False)
	content = db.Column(db.Text, nullable = False)
	datePosted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

