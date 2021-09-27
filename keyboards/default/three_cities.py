from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_city_keyboard(cities: list):
    if not cities:
        return
    buttons = [KeyboardButton(city) for city in cities]
    recent_cities = ReplyKeyboardMarkup([buttons], one_time_keyboard=True)
    return recent_cities
