from flask import request, jsonify
from app import app, db
from app.models import WeatherData

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/weather/insight', methods=['GET'])
def weather_insight():
    condition = request.args.get('condition')
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))

    results = WeatherData.query.filter_by(latitude=lat, longitude=lon).order_by(WeatherData.forecast_time).all()

    insights = []
    for result in results:
        if condition == 'veryHot':
            condition_met = result.temperature > 30
        elif condition == 'rainyAndCold':
            condition_met = result.temperature < 10 and result.precipitation > 0.5
        insights.append({
            'forecastTime': result.forecast_time.isoformat(),
            'conditionMet': condition_met
        })

    return jsonify(insights)

