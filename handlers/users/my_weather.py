from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import location_button
from loader import dp, db
from utils.get_weather_info import get_weather_from_coords


@dp.message_handler(Command('here'))
async def my_weather(message: types.Message):
    await message.answer('Отправьте локацию', reply_markup=location_button.keyboard)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_weather(message: types.Message):
    location = message.location
    latitude, longitude = location.latitude, location.longitude
    weather = get_weather_from_coords(latitude, longitude)
    if weather != "Не нашел такого города :(":
        if weather[1] not in await db.select_three_cities(message.from_user.id):
            await db.insert_user(message.from_user.id, weather[1])
            await db.user_reduction(message.from_user.id)
        await message.answer(weather[0],reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(weather, reply_markup=ReplyKeyboardRemove())
