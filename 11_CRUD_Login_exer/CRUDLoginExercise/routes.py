from flask import render_template, url_for, redirect, request, abort
from CRUDLoginExercise.forms import registrationForm, loginForm, postForm, deleteForm
from CRUDLoginExercise.models import User, Post
from CRUDLoginExercise import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
	posts = Post.query.all()
	return render_template("home.html", posts = posts)

@app.route("/home/<int:postId>")
def homeWithPost(postId):
	post = Post.query.get_or_404(postId)
	posts = Post.query.all()
	return render_template("home.html", post = post, posts = posts)

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

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def newPost():
	form = postForm()
	if form.validate_on_submit():
		post = Post(author = current_user.username, title = form.title.data, content = form.content.data)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('homeWithPost', postId = post.id))
	return render_template('create_post.html', title = 'New post', form = form)

@app.route("/post/update/<int:postId>", methods=['GET', 'POST'])
@login_required
def updatePost(postId):
	post = Post.query.get_or_404(postId)
	if post.author != current_user.username:
		abort(403)
	else:
		form = postForm()
		if form.validate_on_submit():
			post.title = form.title.data
			post.content = form.content.data
			db.session.commit()
			return redirect(url_for('homeWithPost', postId = post.id))
		elif request.method == 'GET':
			form.title.data = post.title
			form.content.data = post.content
			return render_template('create_post.html', title = 'Update post', form = form)
		else:
			return redirect(url_for('home'))

@app.route("/post/delete/<int:postId>", methods=['GET', 'POST'])
@login_required
def deletePost(postId):
	post = Post.query.get_or_404(postId)
	if post.author != current_user.username:
		abort(403)
	else:
		form = deleteForm()
		if form.validate_on_submit():
			db.session.delete(post)
			db.session.commit()
			return redirect(url_for('home'))
		else:
			return render_template('delete_post.html', post = post, form = form)

