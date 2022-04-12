import asyncio
import datetime
import re


from aiogram import types
from loader import dp
from filters import IsGroup, AdminFilter
from aiogram.utils.exceptions import BadRequest
from aiogram.dispatcher.filters.builtin import Command

@dp.message_handler(IsGroup(), Command("Reading", prefixes="!/"), AdminFilter())
async def read(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    command_parse = re.compile(r"(!Reading|/Reading) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 1
    time = int(time)
    until_time = datetime.datetime.now() + datetime.timedelta(minutes=time)
    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_time)
        await message.answer(f"{member.first_name} cannot send messages for {time} minutes for {comment}")
    except BadRequest as err:
        await message.reply(f"Problem occured sir: {err}")


@dp.message_handler(IsGroup(), Command("Unread", prefixes="!/"))
async def unread(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    allowed = types.ChatPermissions(
        can_send_messages=True,
        can_pin_messages=False,
        can_send_media_messages=True,
        can_send_polls=False,
        can_change_info=False,
        can_invite_users=True,
        can_add_web_page_previews=True,
        can_send_other_messages=True
    )
    await message.chat.restrict(user_id=member_id, permissions=allowed, until_date=0)




