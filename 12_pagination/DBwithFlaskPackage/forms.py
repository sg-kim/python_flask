from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from DBwithFlaskPackage.models import User

class RegistrationForm(FlaskForm):	#	this class is inherited from FlaskForm
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])	#	instantiate StringField class
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different username.')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('That email is taken. Please choose a different email address.')

class LoginForm(FlaskForm):	#	this class is inherited from FlaskForm
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class UpdateAccountForm(FlaskForm):	#	this class is inherited from FlaskForm
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])	#	instantiate StringField class
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please choose a different username.')

	def validate_email(self, email):
		if email.data != current_user.email:
			email = User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError('That email is taken. Please choose a different email address.')

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
