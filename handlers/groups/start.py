from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from filters import IsGroup


@dp.message_handler(IsGroup(), Command('start'))
async def echo(message: types.Message):
    name = f'Пух, а не {message.from_user.first_name}' if message.from_user.id == 1526547971 \
        else message.from_user.full_name
    await message.answer('Привет, ' + name + ', это группа!')
