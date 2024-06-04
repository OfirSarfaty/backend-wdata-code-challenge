import sys
import os
from app import create_app, db
from app.models import WeatherData

app = create_app()

with app.app_context():
    db.create_all()
