from flask import render_template, Blueprint, make_response, request

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def	home():
	resp = make_response(render_template("home.html"))
	resp.set_cookie("userID", "12345")

	return resp

@main.route("/getCookie")
def getCookie():
	userID = request.cookies.get("userID")

	return 'user ID is ' + userID

@main.route("/delCookie")
def delCookie():
	resp = make_response("deleting cookie")
	resp.set_cookie("userID", '', expires = 0)

	return resp

