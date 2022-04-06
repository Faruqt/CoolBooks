import flask_sqlalchemy
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()
class User(db.Model):
	__tablename__ = 'cool_user'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), unique=True, nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	first_name = db.Column(db.String(255), unique=False, nullable=True)
	last_name = db.Column(db.String(255), unique=False, nullable=True)
	password = db.Column(db.String(255), unique=False, nullable=False)

