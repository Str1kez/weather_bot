# import io

from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import InputFile
from utils.db_api import select_cities, insert_user, user_reduction
from utils.get_weather_info import get_weather
from loader import dp


# хендлит фото
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def download_photo(message: types.Message):
#     await message.reply(message.photo[0].file_id)
#
#
# В ответ на документ, скидывает картинку, айди брал из хендлера выше
# @dp.message_handler(content_types=types.ContentType.DOCUMENT)
# async def download_photo(message: types.Message):
#     await message.answer_photo('AgACAgIAAxkBAAIEfWE9EPsDfn6WNqtQaTaTn4BZKInvAAJPtjEbtSDoSYDBa-_BvIcHAQADAgADcwADIAQ',
#                                'That picture from you',
#                                'HTML')

# хендлер, который скачивает в байты пикчу и отправляет скачанную в ответ
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_downloaded_photo(message: types.Message):
#     byte = io.BytesIO()
#     await message.photo[0].download(byte)
#     await message.answer('Я получил ваше фото, сейчас отправлю его')
#     photo = InputFile(byte)
#     await message.answer_photo(photo, 'your picture', 'HTML')


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler()
async def bot_weather(message: types.Message):
    weather = get_weather(message.text)
    if weather != "Не нашел такого города :(":
        if weather[1] not in await select_cities(message.from_user.id):
            await insert_user(message.from_user.id, weather[1])
            await user_reduction(message.from_user.id)
        await message.answer(weather[0])
    else:
        await message.answer(weather)
    # is_c_mem = await bot.get_chat_member(-1001529367317, message.from_user.id)
    # is_member = not (is_c_mem['status'] == 'left')
    # await message.answer(str(is_member))


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_weather_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
