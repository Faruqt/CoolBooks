import flask_sqlalchemy
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

class ExchangeRequest(db.Model):
	__tablename__ = 'exchange'
	
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	book_title = db.Column(db.String(255))
	author = db.Column(db.String(255))
	description = db.Column(db.String(255))
	cover_pic = db.Column(db.String(255))
	type = db.Column(db.String(255))
	wanted_type = db.Column(db.String(255))
	request_matched = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<{} Book>'.format(self.title)

	def to_json(self):
		return {
				'id': self.id,
				'user_id':self.user_id,
				'title': self.book_title,
				'author': self.author,
				'description': self.description,
				'cover_pic': self.cover_pic,
				'type_tag':self.type,
				'wanted_type':self.wanted_type
			}
