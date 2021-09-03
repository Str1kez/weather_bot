from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), Command('help'))
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/weather - Сначала отправь город, затем ответь на свое сообщение с данной командой")
    await message.answer('\n'.join(text))
