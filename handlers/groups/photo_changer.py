from aiogram import types
import io
from loader import dp, bot
from aiogram.dispatcher.filters.builtin import Command
from filters import AdminFilter, IsGroup

@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def photo(message: types.Message):
    source_message = message.reply_to_message
    print(source_message)
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await bot.set_chat_photo(message.chat.id, photo=input_file)

