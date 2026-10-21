import requests
import os

URL = 'http://api.weatherapi.com/v1/current.json'
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY is not set")


def get_weather(city):
    try:
        resp = requests.get(
            URL,
            params={'key': API_KEY, 'q': city, 'aqi': 'yes'}
        )
    except requests.RequestException:
        return f"Could not reach the exchange rate service to check weather"
    data = resp.json()
    if resp.status_code != 200 or not data.get('success', True):
        return f"Could not get weather in {city}"
    location = data.get("location", {})
    current = data.get("current", {})
    condition = current.get("condition", {})
    city_name = location.get("name", city)
    temperature = current.get("temp_c")
    condition_text = condition.get("text")
    humidity = current.get("humidity")
    wind_speed = current.get("wind_kph")

    return (
        f"City: {city_name}, "
        f"Temperature: {temperature}°C, "
        f"Condition: {condition_text}, "
        f"Humidity: {humidity}%, "
        f"Wind speed: {wind_speed} kph"
    )


TOOLS = {
    "get_weather": get_weather,
}