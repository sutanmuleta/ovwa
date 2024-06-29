import requests

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
    
    # Extracting necessary information
    forecast = data["forecast"]["forecastday"][0]
    temperature = forecast["day"]["avgtemp_c"]
    condition = forecast["day"]["condition"]["text"]

    return temperature, condition

# Example usage
city = "Seattle"
date = "2024-07-01"
temperature, condition = get_weather(city, date)
if temperature is not None and condition is not None:
    print(f"The average temperature in {city} on {date} will be {temperature}°C with {condition} conditions.")
