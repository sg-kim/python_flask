from flask import Flask
from cookieAndSession.config import Config
from flask_sqlalchemy import SQLAlchemy
from cookieAndSession.main.utils import SQLAlchemySessionInterface

db = SQLAlchemy()

def create_app(config_class = Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)

	from cookieAndSession.main.routes import main

	app.register_blueprint(main)

	app.session_interface = SQLAlchemySessionInterface()

	return app

