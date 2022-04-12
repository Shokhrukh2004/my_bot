from aiogram import types
from loader import dp
from filters import AdminFilter

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Yes sir!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Sorry {message.from_user.first_name.title()} I didn't understand🥺")

