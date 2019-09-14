from flask import render_template, url_for, redirect, request
from CRUDLoginExercise.forms import registrationForm, loginForm
from CRUDLoginExercise.models import User
from CRUDLoginExercise import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = registrationForm()
	if form.validate_on_submit():
		hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email = form.email.data, password = hashedPassword)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template("register.html", title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = loginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			nextPage = request.args.get('next')
			return redirect(nextPage) if nextPage else redirect(url_for('home'))
	return render_template("login.html", title = 'Login', form = form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

