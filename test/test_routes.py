import unittest
from app import app
import json
import pandas as pd
from sqlalchemy import create_engine


class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Flask app is running!")

    def sort_by_forecast_time(self, item):
        return item['forecastTime']

    def test_weather_insight_very_hot(self):
        tester = app.test_client(self)
        response = tester.get('/weather/insight?lon=51.5&lat=24.5&condition=veryHot')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        expected_response = [
            {"forecastTime": "2021-04-02T13:00:00", "conditionMet": True},
            {"forecastTime": "2021-04-02T14:00:00", "conditionMet": True},
            {"forecastTime": "2021-04-02T15:00:00", "conditionMet": False}
        ]
        response.json.sort(key=self.sort_by_forecast_time)
        expected_response.sort(key=self.sort_by_forecast_time)
        self.assertEqual(response.json, expected_response)

    def test_weather_insight_rainy_and_cold(self):
        tester = app.test_client(self)
        response = tester.get('/weather/insight?lon=51.5&lat=24.5&condition=rainyAndCold')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        expected_response = [
            {"forecastTime": "2021-04-02T13:00:00", "conditionMet": False},
            {"forecastTime": "2021-04-02T14:00:00", "conditionMet": False},
            {"forecastTime": "2021-04-02T15:00:00", "conditionMet": True}
        ]
        response.json.sort(key=self.sort_by_forecast_time)
        expected_response.sort(key=self.sort_by_forecast_time)
        self.assertEqual(response.json, expected_response)

    def test_all_data_inserted(self):
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

        df1 = pd.read_csv('data/file1.csv')
        df2 = pd.read_csv('data/file2.csv')
        df3 = pd.read_csv('data/file3.csv')

        df1.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
        df2.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']
        df3.columns = ['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']

        df3['precipitation'] = df3['precipitation'] * 25.4

        csv_data = pd.concat([df1, df2, df3])
        csv_data['forecast_time'] = pd.to_datetime(csv_data['forecast_time'])
        db_data = pd.read_sql_table('weather_data', engine)

        # Ensure the data matches
        pd.testing.assert_frame_equal(csv_data.reset_index(drop=True), db_data[['longitude', 'latitude', 'forecast_time', 'temperature', 'precipitation']].reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()
