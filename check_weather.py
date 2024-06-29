import requests
from datetime import datetime, timedelta

API_KEY = "d3f1511662044817a10193525242906"
BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

def get_weather(city, date):
    # Construct the URL with the city and date parameters
    url = f"{BASE_URL}?key={API_KEY}&q={city}&dt={date}"
    
    # Make the API call
    response = requests.get(url)
    
    # Check for errors in the response
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
    # Parse the JSON response
    data = response.json()
    
    if "error" in data:
        print(f"Error: {data['error']['message']}")
        return None
    
    # Extracting hourly forecast data for the specified date
    forecast = data["forecast"]["forecastday"][0]["hour"]
    return forecast

def print_weather_every_3_hours(city, start_date, end_date):
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        forecast = get_weather(city, date_str)
        
        if not forecast:
            current_date += delta
            continue

        print(f"Weather forecast for {city} on {date_str} every 3 hours:")
        for i in range(0, len(forecast), 3):
            hour_data = forecast[i]
            time = hour_data["time"]
            temp_c = hour_data["temp_c"]
            condition = hour_data["condition"]["text"]
            print(f"At {time}: Temperature: {temp_c}°C, Condition: {condition}")
        current_date += delta

# Example usage
# city = "Seattle"
# start_date = "2024-07-01"
# end_date = "2024-07-03"
# print_weather_every_3_hours(city, start_date, end_date)

# check_weather.py