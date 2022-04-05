from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .api import ub as user_blueprint
        app.register_blueprint(user_blueprint)
        return app
