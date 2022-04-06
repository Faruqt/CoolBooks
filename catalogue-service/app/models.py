import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
class Catalogue(db.Model):
	__tablename__ = 'catalogue'
	
	id = db.Column(db.Integer, primary_key=True)
	book = db.Column(db.String(255), unique=True, nullable=False)
