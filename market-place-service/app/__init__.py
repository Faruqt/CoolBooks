from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .api import mb as market_blueprint
        app.register_blueprint(market_blueprint)
        return app
