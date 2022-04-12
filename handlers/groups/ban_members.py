from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import Command
from filters import IsGroup, AdminFilter


@dp.message_handler(IsGroup(), Command("Ban members", prefixes="!/"), AdminFilter())
async def bann(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    await message.chat.kick(user_id=member_id)

@dp.message_handler(IsGroup(), Command("Unban members", prefixes="!/"), AdminFilter())
async def unbann(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    await message.chat.unban(user_id=member_id)
