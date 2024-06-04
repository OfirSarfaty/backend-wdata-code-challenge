import sys
import os
import pandas as pd
from sqlalchemy import create_engine

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import WeatherData

def ingest_data():
    app = create_app()
    with app.app_context():
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        df1 = pd.read_csv('data/file1.csv')
        df2 = pd.read_csv('data/file2.csv')
        df3 = pd.read_csv('data/file3.csv')

        # Standardize column names
        df1.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
        df2.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
        df3.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
        
        # Convert precipitation from inches to mm for file3
        df3['precipitation'] = df3['precipitation'] * 25.4

        weather_data = pd.concat([df1, df2, df3])
        weather_data['forecast_time'] = pd.to_datetime(weather_data['forecast_time'])
        weather_data.to_sql('weather_data', engine, if_exists='append', index=False)

if __name__ == '__main__':
    ingest_data()
