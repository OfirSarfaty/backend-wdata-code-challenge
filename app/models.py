from app import db

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    forecast_time = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    precipitation = db.Column(db.Float, nullable=False)
