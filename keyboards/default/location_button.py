from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup([
    [
        KeyboardButton(text='📍', request_location=True)
    ]
], resize_keyboard=True)
