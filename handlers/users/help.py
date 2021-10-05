from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/send_contact - Написать контакты боту, он их выведет",
            '/recent (/close_recent) - Выведет или закроет меню с 3 городами',
            '/here - Погода по локации',
            "Пиши название города на русском или английском языке")
    await message.answer("\n".join(text))
