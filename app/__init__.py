from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('WEATHER_SERVICE_DATABASE_URL', 'postgresql://weatheruser:asdfg@localhost/weatherdb')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Import routes inside the app context to avoid circular imports
        from . import routes

    return app
