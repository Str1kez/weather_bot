from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import get_city_keyboard
from loader import dp
from utils.db_api import select_cities


@dp.message_handler(Command('recent'))
async def get_recent_cities(message: types.Message):
    await message.answer('Выбери город',
                         reply_markup=get_city_keyboard(await select_cities(message.from_user.id)))


@dp.message_handler(Command('close_recent'))
async def close_recent(message: types.Message):
    await message.answer('<b>Города убраны</b>', reply_markup=ReplyKeyboardRemove())
