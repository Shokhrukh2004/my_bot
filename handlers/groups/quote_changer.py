from aiogram import types
from loader import dp, bot
from filters import IsGroup, AdminFilter
from aiogram.dispatcher.filters.builtin import Command

@dp.message_handler(IsGroup(), Command("set_quote", prefixes="!/"), AdminFilter())
async def quote(message: types.Message):
    source_quote = message.reply_to_message
    quote = source_quote.text
    await bot.set_chat_description(message.chat.id, description=quote)
