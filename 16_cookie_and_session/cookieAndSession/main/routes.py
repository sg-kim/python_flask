from flask import render_template, Blueprint, request, session
from cookieAndSession.models import FlaskSession
from cookieAndSession import db

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def	home():
	session['username'] = 'Lisa'

	return 'session이 만들어졌습니다.'

@main.route("/getSessionData")
def getSessionData():
	username = session.get('username')

	return 'username은 ' + username + ' 입니다.'

@main.route("/delSession")
def	delSession():
	session.clear()

	return 'session이 삭제되었습니다.'

