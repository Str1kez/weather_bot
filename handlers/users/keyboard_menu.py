from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите город', reply_markup=menu)


@dp.message_handler(Command('close_menu'))
async def close_menu(message: types.Message):
    await message.answer(reply_markup=ReplyKeyboardRemove(), text='<b>Меню убрано</b>')
