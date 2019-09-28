from cookieAndSession import db

class FlaskSession(db.Model):

	sid = db.Column(String, primary_key = True)
	value = db.Column(BLOB)

	@classmethod
	def change(cls, sid, value):
		rec = db.query(cls).filter(cls.sid == sid).first()
		if not rec:
			rec = cls()
			rec.sid = sid
		rec.value = value

		return rec

