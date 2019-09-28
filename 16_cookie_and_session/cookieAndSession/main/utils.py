from flask import request
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin
import pickle
from uuid import uuid4
from cookieAndSession.models import FlaskSession

class SQLAlchemySession(CallbackDict, SessionMixin):
	def __init__(self, initial = None, sid = None, new = False):
		def on_update(self):
			self.modified = True
		CallbackDict.__init__(self, initial, on_update)
		self.sid = sid
		self.new = new
		self.modified = False

class SQLAlchemySessionInterface(SessionInterface):
	session_class = SQLAlchemySession
	serializer = pickle

	def generate_sid(self):
		return str(uuid4())

	def open_session(self, app, request):
		sid = request.cookies.get(app.session_cookie_name)
		if not sid:
			sid = self.generate_sid()
			return self.session_class(sid = sid, new = True)

		rec = db.query(FlaskSession).filter(FlaskSession.sid == sid).first()

		if rec is not None:
			data = self.serializer.loads(rec.value)
			return self.session_class(data, sid = sid)

		return self.session_class(sid = sid, new = True)

	def save_session(self, app, session, response):
		domain  = self.get_cookie_domain(app)
		if not session:
			rec = db.query(FlaskSession).filter(FlaskSession.sid == session.sid).first()
			db.delete(rec)
			db.commit()
			if session.modified:
				make_response.delete_cookie(app.session_cookie_name, domain = domain)
			return
		val = self.serializer.dumps(dict(session))
		session_db = FlaskSession.change(session.sid, val)
		db.add(session_db)
		db.commit()

		httponly = self.get_cookie_httponly(app)
		secure = self.get_cookie_secure(app)
		expires = self.get_expiration_time(app, session)

		make_response.set_cookie(app.session_cookie_name, session.sid, expires = expires, httponly = httponly, domain = domain, secure = secure)


