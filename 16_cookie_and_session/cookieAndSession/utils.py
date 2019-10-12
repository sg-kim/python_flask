from flask import request
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin
import pickle
from uuid import uuid4
from cookieAndSession import db
from cookieAndSession.models import FlaskSession
from sqlalchemy import create_engine
from cookieAndSession.config import Config

class SQLAlchemySession(CallbackDict, SessionMixin):
	def __init__(self, initial = None, sid = None, new = False):
		def on_update(self):
			print('SQLAlchemySession.on_update')
			self.modified = True
		CallbackDict.__init__(self, initial, on_update)
		self.sid = sid
		self.new = new
		self.modified = False
	
		engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

		if not engine.dialect.has_table(engine, 'flask_session'):
			db.create_all()
			print('table for session is created.')

		engine.dispose()

class SQLAlchemySessionInterface(SessionInterface):
	session_class = SQLAlchemySession
	serializer = pickle

	def generate_sid(self):
		return str(uuid4())

	def open_session(self, app, request):
		sid = request.cookies.get(app.session_cookie_name)
		if not sid:
			print('SQLAlchemySessionInterface.open_session.if_not_sid')
			sid = self.generate_sid()
			return self.session_class(sid = sid, new = True)

		rec = db.session.query(FlaskSession).filter(FlaskSession.sid == sid).first()

		if rec is not None:
			print('SQLAlchemySessionInterface.open_session.if_rec_is_not_None')
			data = self.serializer.loads(rec.value)
			return self.session_class(data, sid = sid)
		
		print('SQLAlchemySessionInterface.open_session')

		return self.session_class(sid = sid, new = True)

	def save_session(self, app, session, response):
		domain = self.get_cookie_domain(app)
		if not session:
			print('SQLAlchemySessionInterface.save_session.if_not_session')
			rec = db.session.query(FlaskSession).filter(FlaskSession.sid == session.sid).first()
			if rec is not None:
				db.session.delete(rec)
				db.session.commit()
			if session.modified:
				response.delete_cookie(app.session_cookie_name, domain = domain)
			return
		print('SQLAlchemySessionInterface.save_session')
		val = self.serializer.dumps(dict(session))
		session_db = FlaskSession.change(session.sid, val)
		db.session.add(session_db)
		db.session.commit()

		httponly = self.get_cookie_httponly(app)
		secure = self.get_cookie_secure(app)
		expires = self.get_expiration_time(app, session)

		response.set_cookie(app.session_cookie_name, session.sid, expires = expires, httponly = httponly, domain = domain, secure = secure)


