import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsAdmin, IsGroup
from loader import dp


@dp.message_handler(IsAdmin(), IsGroup(), Command('ro'))
async def set_read_only(message: types.Message):
    user = message.reply_to_message.from_user
    time = int(message.text.split()[-1])
    until_time = datetime.datetime.now() + datetime.timedelta(minutes=time)
    permissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
    )
    await message.answer(user.first_name + ' нельзя писать в течение ' + str(time) + ' минут')
    # await bot.restrict_chat_member(chat.id, user.id, permissions, until_time)
    await message.chat.restrict(user.id, permissions, until_time)


@dp.message_handler(IsAdmin(), IsGroup(), Command('unro'))
async def undo_read_only(message: types.Message):
    user = message.reply_to_message.from_user
    permissions = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
    )
    await message.answer(user.first_name + ' снова может писать')
    await message.chat.restrict(user.id, permissions, until_date=0)
