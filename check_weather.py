# check_weather.py

import requests
from datetime import datetime, timedelta

API_KEY = "d3f1511662044817a10193525242906"
BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

def get_weather(city, date):
    url = f"{BASE_URL}?key={API_KEY}&q={city}&dt={date}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    if "error" in data:
        return None
    forecast = data["forecast"]["forecastday"][0]["hour"]
    return forecast

def print_weather_every_3_hours(city, start_date, end_date):
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)

    weather_info = ""

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        forecast = get_weather(city, date_str)
        
        if not forecast:
            current_date += delta
            continue

        weather_info += f"Weather forecast for {city} on {date_str} every 3 hours:\n"
        for i in range(0, len(forecast), 3):
            hour_data = forecast[i]
            time = hour_data["time"]
            temp_c = hour_data["temp_c"]
            condition = hour_data["condition"]["text"]
            weather_info += f"At {time}: Temperature: {temp_c}°C, Condition: {condition}\n"
        
        current_date += delta
    
    return weather_info
