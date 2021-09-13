from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputMessageContent, InlineQueryResultPhoto

from loader import dp
# from utils import get_pictures


# @dp.inline_handler()
# async def show_pictures(query: types.InlineQuery):
#     results = get_pictures(query.query, 20)
#     print(query.offset)
#     await query.answer(results=results, cache_time=10)


@dp.inline_handler(text='города')
async def start_required(query: types.InlineQuery):
    print(query.offset)
    await query.answer(results=[
        InlineQueryResultPhoto(id='Kazan',
                               photo_url='https://planetofhotels.com/guide/sites/default/files/styles/paragraph'
                                         '__live_banner__lb_image__1880bp/public/live_banner/Kazan-1.jpg',
                               caption='Казань, Кремль',
                               title='Казань',
                               description='Кремль, Кул-Шариф',
                               thumb_url='https://tcf.admeen.org/game/17500/17296/400x246/cars-lightning-speed.jpg'),
        InlineQueryResultPhoto(id='Los-Angeles',
                               photo_url='https://images.musement.com/cover/0001/43/los-angeles_header-42380.'
                                         'jpeg?w=1200&h=630&q=95&fit=crop',
                               caption='Los-Angeles',
                               thumb_url='https://s.rdrom.ru/1/pubs/4/38866/2021384.jpg',
                               description='город в США',
                               title='Los-Angeles'),
        InlineQueryResultPhoto(id='Moscow',
                               title='Москва',
                               caption='Москва, Красная площадь',
                               description='Красная площадь',
                               photo_url='https://www.planete-energies.com/sites/default/files/styles/'
                                   'media_full_width_940px/public/thumbnails/image/moscow.jpg?itok=J_vRU4rA',
                               thumb_url='https://www.planete-energies.com/sites/default/files/styles/'
                                     'media_full_width_940px/public/thumbnails/image/moscow.jpg?itok=J_vRU4rA'),
        # InlineQueryResultArticle(id='Москва', title='Moscow',
        #                          input_message_content=InputMessageContent(message_text='About Moscow'),
        #                          url='https://www.planete-energies.com/sites/default/files/styles/'
        #                              'media_full_width_940px/public/thumbnails/image/moscow.jpg?itok=J_vRU4rA',
        #                          thumb_url='https://www.planete-energies.com/sites/default/files/styles/'
        #                                    'media_full_width_940px/public/thumbnails/image/moscow.jpg?itok=J_vRU4rA',
        #                          hide_url=True,
        #                          description='Red square, Moscow'
        #                          )
    ],
        cache_time=5,
        switch_pm_text='need to start',
        switch_pm_parameter='default')
