from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .api import cb as catalogue_blueprint
        app.register_blueprint(catalogue_blueprint)
        return app
