from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Kazan'),
            KeyboardButton(text='Moscow'),
        ],
        [
            KeyboardButton(text='Los Angeles')
        ]
    ],
    resize_keyboard=True
)
