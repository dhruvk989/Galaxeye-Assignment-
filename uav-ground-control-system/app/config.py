# Store configuration values like database URI and paths
import os

class Config:
    # This is where the configurations for your app go
    # For now, we'll configure the SQLAlchemy database URI

    # SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uav_database.db'
    
    # Disable modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management (replace with a secure key in production)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
