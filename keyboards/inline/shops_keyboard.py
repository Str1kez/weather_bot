from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .shops_datas import shops_callback


shops = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                                  [
                                    InlineKeyboardButton('Asos', callback_data=shops_callback.new(
                                        shop='asos', country='england')),
                                    InlineKeyboardButton('Adidas', callback_data='get:adidas:germany'),
                                    InlineKeyboardButton('Farfetch', callback_data='get:farfetch:sweden')
                                  ]
                              ])


adidas_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Ссылка:', url='https://www.adidas.ru/')
    ]
])

asos_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Ссылка:', url='https://www.asos.com/ru/men/')
    ]
])

farfetch_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Ссылка:', url='https://www.farfetch.com/ru/')
    ]
])
