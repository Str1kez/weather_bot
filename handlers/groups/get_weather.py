from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from loader import dp
from utils.get_weather_info import get_weather


@dp.message_handler(IsGroup(), Command('weather'))
async def user_weather(message: types.Message):
    reply_text = message.reply_to_message.text
    await message.answer(get_weather(reply_text))
