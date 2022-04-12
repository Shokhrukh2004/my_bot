from loader import dp
from aiogram import types
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart

@dp.message_handler(CommandStart(), chat_id=ADMINS)
async def star(message: types.Message):
    await message.reply("I started my job Boss!")

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.reply(f"Welcome dear {message.from_user.first_name.title()}!")

