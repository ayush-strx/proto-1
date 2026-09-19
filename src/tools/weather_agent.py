import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

TOOL_NAME = "weather_agent"
TOOL_DESCRIPTION = (
    "Provides real-time weather information for any city, including temperature, "
    "how it feels, and general conditions like rain, clouds, or sunshine. "
    "Use this whenever the user asks about current weather, temperature, "
    "climate, or whether it's raining/sunny/cold/hot somewhere."
)
TOOL_PARAMETER = "the name of the city"


def get_weather(city):
    if not city:
        return "Please specify a city name."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            return f"The weather in {city} is {temp} degrees Celsius, feels like {feels_like} degrees, with {description}."
        elif response.status_code == 404:
            return f"Sorry, I couldn't find a city called {city}."
        else:
            return "Sorry, something went wrong while fetching the weather."

    except requests.exceptions.RequestException:
        return "Sorry, I couldn't connect to the weather service."