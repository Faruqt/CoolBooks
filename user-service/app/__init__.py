from flask import Flask
from .models import db
from . import config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = config.ACCESS_TOKEN_EXPIRES

    db.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()
        from .api import ub as user_blueprint
        app.register_blueprint(user_blueprint)
        return app
