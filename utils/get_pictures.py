import json
import logging

import requests
from aiogram.types import InlineQueryResultPhoto

from data.config import PEXELS_API


def get_json(city: str, per_page: int):
    r_params = {
        'page': 1,
        'query': city,
        'locale': 'ru-RU',
        'size': 'small',
        'per_page': per_page
    }
    r = requests.get('https://api.pexels.com/v1/search',
                     params=r_params, headers={'Authorization': PEXELS_API})
    return r.json()


def get_pictures(city: str, per_page: int) -> list:
    raw_data = get_json(city, per_page)
    # raw_data = json.load(open('utils/test.json', 'r', encoding='utf-8'))
    json.dump(raw_data, open('utils/test.json', 'w'))
    if 'photos' not in raw_data:
        if 'error' in raw_data:
            logging.exception(f'Что-то не так с API по картинкам: {raw_data["error"]}')
        return []
    result = []
    for pic in raw_data['photos']:
        res_photo = InlineQueryResultPhoto(
            id=pic['id'],
            caption=city,
            description='...',
            title='...',
            photo_url=pic['src']['medium'],
            # photo_url='https://planetofhotels.com/guide/sites/default/files/styles/paragraph'
            #         '__live_banner__lb_image__1880bp/public/live_banner/Kazan-1.jpg',
            thumb_url=pic['src']['small']
        )
        result.append(res_photo)
    return result
