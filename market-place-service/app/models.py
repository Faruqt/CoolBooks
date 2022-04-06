import flask_sqlalchemy
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()
class Market(db.Model):
	__tablename__ = 'market'
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	author = db.Column(db.String(255))
	descr = db.Column(db.String(255))
	cover_pic = db.Column(db.String(255))

	def __repr__(self):
		return '<{} Book>'.format(self.title)
