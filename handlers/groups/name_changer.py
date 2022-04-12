from aiogram import types
from loader import dp, bot
from filters import IsGroup, AdminFilter
from aiogram.dispatcher.filters.builtin import Command

@dp.message_handler(IsGroup(), Command("set_name", prefixes="!/"), AdminFilter())
async def name(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await bot.set_chat_title(message.chat.id, title=title)