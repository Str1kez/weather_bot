from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputMessageContent, InlineQueryResultPhoto

from loader import dp


@dp.inline_handler()
async def start_required(query: types.InlineQuery):
    await query.answer(results=[
        InlineQueryResultPhoto(id='Ferrari',
                               photo_url='https://www.a777aa77.ru/ferrari/2015-ferrari-fxx-k.jpg',
                               caption='Ferrari FXX K',
                               thumb_url='https://tcf.admeen.org/game/17500/17296/400x246/cars-lightning-speed.jpg')
    ],
        cache_time=5,
        switch_pm_text='need to start',
        switch_pm_parameter='default')
