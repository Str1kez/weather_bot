import requests
from data.config import WEATHER_API
from datetime import datetime as dt


def get_request(city: str):
    result = requests.get("https://api.openweathermap.org/data/2.5/weather",
                          params={'q': city, 'units': 'metric', 'appid': WEATHER_API, 'lang': 'ru'})
    return result.json()


def get_weather(city: str):
    req = get_request(city)
    if req['cod'] != 200:
        return "Не нашел такого города :("
    return put_weather(req)


def put_weather(status: dict):
    time = dt.fromtimestamp(status['dt'] + status['timezone'] - 10800)
    time = time.time()
    temp = round(status["main"]["temp"])
    temp_feels = round(status['main']['feels_like'])
    state = status["weather"][0]["description"]
    city_info = "В городе {} сейчас {} часов.".format(status['name'], time.isoformat(timespec='minutes'))
    weather_info = "На улице {} °C, ощущается как {} °C".format(temp, temp_feels)
    wind_info = "Скорость ветра {} м/сек".format(status['wind']['speed'])
    state_info = state.capitalize()
    return "\n".join((city_info, weather_info, wind_info, state_info))
