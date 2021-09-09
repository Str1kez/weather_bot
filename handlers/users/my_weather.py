from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import location_button
from loader import dp
from utils.get_weather_info import get_weather_from_coords


@dp.message_handler(Command('here'))
async def my_weather(message: types.Message):
    await message.answer('Отправьте локацию', reply_markup=location_button.keyboard)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_weather(message: types.Message):
    location = message.location
    latitude, longitude = location.latitude, location.longitude
    await message.answer(get_weather_from_coords(latitude, longitude), reply_markup=ReplyKeyboardRemove())
