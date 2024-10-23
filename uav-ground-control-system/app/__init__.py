from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Import routes
    from .routes import app as routes_app
    app.register_blueprint(routes_app)

    return app
