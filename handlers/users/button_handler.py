from aiogram import types
from loader import dp
from keyboards.default.language_wiki import lang_key
from keyboards.default.Menu import menu_keys
from keyboards.default.bot_info import BotInfo
from keyboards.default.currency_menu import curr_ency
from keyboards.inline.books import bookss
from filters import IsPrivate

@dp.message_handler(IsPrivate(), text='Search Wikipedia')
async def set_lang(message: types.Message):
    await message.answer("Choose the Language", reply_markup=lang_key)

@dp.message_handler(IsPrivate(),text=['Ortga Qaytish!', 'Go back!'])
async def go_back(message: types.Message):
    await message.answer('Choose again! ', reply_markup=menu_keys)

@dp.message_handler(IsPrivate(), text='Bot info')
async def bot_info(message: types.Message):
    await message.answer('Good job!', reply_markup=BotInfo)

@dp.message_handler(IsPrivate(), text='Check the Currency')
async def currency(message: types.message):
    await message.answer('Choose the Currency!', reply_markup=curr_ency)

@dp.message_handler(IsPrivate(), text="Books --- Kitoblar")
async def books(message: types.Message):
    await message.answer("Good job! ", reply_markup=bookss)

