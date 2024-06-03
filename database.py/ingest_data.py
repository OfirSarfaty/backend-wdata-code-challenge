import sys
import os
import pandas as pd
from sqlalchemy import create_engine

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from app.models import WeatherData

def ingest_data():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    file1 = pd.read_csv('data/file1.csv')
    file2 = pd.read_csv('data/file2.csv')
    file3 = pd.read_csv('data/file3.csv')

    # Standardize column names
    file1.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
    file2.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
    file3.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
    
    # Convert precipitation from inches to mm for file3
    file3['precipitation'] = file3['precipitation'] * 25.4

    weather_data = pd.concat([file1, file2, file3])
    weather_data['forecast_time'] = pd.to_datetime(weather_data['forecast_time'])
    weather_data.to_sql('weather_data', engine, if_exists='append', index=False)

if __name__ == '__main__':
    with app.app_context():
        ingest_data()
