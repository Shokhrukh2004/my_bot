from aiogram import types
from loader import dp


@dp.message_handler(text='Bot Haqida Malumot')
async def bot_info(message: types.Message):
    await message.answer(f'Salom {message.from_user.first_name.title()}, Men Multi_bot man\nQulimdan Quyidagilar keladi: Wikipedia,   valyuta kurslari,    Elon berish!')

@dp.message_handler(text="Info about Bot")
async def bot_info(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name.title()}, i am Multi_bot.\nI can do: Wikipedia,     Currency,    Sell Car!')

@dp.message_handler(text="Bot boshqaruvchi bilan bog'lanish!")
async def owner(message: types.Message):
    await message.answer("Bot yaratuvchining telefon raqami: +998933397730")
    await message.answer("<a href='https://t.me/Shoxrux_55555'>Shoxrux!</a>")



@dp.message_handler(text="Approach the bot owner!")
async def owner(message: types.Message):
    await message.answer("Bot creator's number: +998933397730")
    await message.answer("<a href='https://t.me/Shoxrux_55555'>Shoxrux</a>")