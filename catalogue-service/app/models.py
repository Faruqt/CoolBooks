import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
class Catalogue(db.Model):
	__tablename__ = 'catalogue'
	
	id = db.Column(db.Integer, primary_key=True)
	book_title = db.Column(db.String(255), unique=True)
	author = db.Column(db.String(255))
	description = db.Column(db.String(255))
	cover_pic = db.Column(db.String(255))

	def __repr__(self):
		return '<{} Book>'.format(self.title)
		
	def to_json(self):
		return {
				'id': self.id,
				'title': self.book_title,
				'author': self.author,
				'description': self.description,
				'cover_pic': self.cover_pic
			}
