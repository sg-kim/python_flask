from flask import Flask

app = Flask(__name__)	# name is a special variable that gets module name

@app.route("/")
@app.route("/home")
def hello():
	return "<h1>Hello Flask!</h1>"

if __name__ == "__main__":
	app.run("172.17.64.182")
