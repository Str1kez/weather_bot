from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline import shops, shops_callback, adidas_link, farfetch_link, asos_link
from loader import dp


@dp.message_handler(Command('get_shops'))
async def get_shops(message: types.Message):
    await message.answer('Выберите магазин', reply_markup=shops)


@dp.callback_query_handler(shops_callback.filter(shop='asos'))
async def get_adidas(call: CallbackQuery, callback_data: dict):
    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.answer(f'Вы выбрали {callback_data["shop"]}', reply_markup=asos_link)


@dp.callback_query_handler(shops_callback.filter(shop='adidas'))
async def get_adidas(call: CallbackQuery, callback_data: dict):
    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.answer(f'Вы выбрали {callback_data["shop"]}', reply_markup=adidas_link)


@dp.callback_query_handler(shops_callback.filter(shop='farfetch'))
async def get_adidas(call: CallbackQuery, callback_data: dict):
    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.answer(f'Вы выбрали {callback_data["shop"]}', reply_markup=farfetch_link)
