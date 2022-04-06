from flask import Flask
from .models import db
from . import config

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        from .api import mb as market_blueprint
        app.register_blueprint(market_blueprint)
        return app

