from flask import Flask
import os
import cloudinary
from .models import db
from . import config

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
                  api_secret=os.getenv('API_SECRET'))

    db.init_app(app)

    with app.app_context():
        db.create_all()
        from .api import cb as catalogue_blueprint
        app.register_blueprint(catalogue_blueprint)
        return app

