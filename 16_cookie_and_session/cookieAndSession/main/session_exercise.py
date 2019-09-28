from flask import render_template, Blueprint, make_response, request, session

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def	home():
	session['userID'] = '67890'

	return render_template("home.html")

@main.route("/getSession")
def getSession():
	if 'userID' in session:
		userID = session['userID']

	return 'user ID is ' + userID

@main.route("/delSession")
def delSession():
	session.pop('userID', None)

	return 'deleting session'

