from flask import Flask
from cookieAndSession.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

print('__init__ ' + __name__)

def create_app(config_class = Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	print('create_app ' + __name__)

	db.init_app(app)

	from cookieAndSession.main.routes import main

	app.register_blueprint(main)

	from cookieAndSession.utils import SQLAlchemySessionInterface

	app.session_interface = SQLAlchemySessionInterface()

	return app

