from aiogram import types

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member_notification(message: types.Message):
    new_members = (member.get_mention() for member in message.new_chat_members)
    await message.answer(f'Приветствуем чемпионов:\n{", ".join(new_members)}')


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_member_notification(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer('Не уходи, ', message.left_chat_member.get_mention(as_html=True))
    else:
        await message.answer(message.left_chat_member.get_mention(as_html=True) + ' был удален '
                             + message.from_user.get_mention(as_html=True))
