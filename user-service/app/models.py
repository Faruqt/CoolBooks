import flask_sqlalchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = flask_sqlalchemy.SQLAlchemy()
class User(db.Model):
	__tablename__ = 'cool_user'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	first_name = db.Column(db.String(255), unique=False)
	last_name = db.Column(db.String(255), unique=False)
	password_hash = db.Column(db.String(255))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def from_dict(data):
		for field in ['first_name', 'last_name', 'username', 'email']:
			if field in data:
				if data[field] is not None:
					setattr(self, field, data[field].lower())
		if 'password' in data:
			self.set_password(data['password'])

	def to_json(self):
		return {
				'id': self.id,
				'first_name': self.first_name,
				'last_name': self.last_name,
				'username': self.username,
				'email': self.email
			}


