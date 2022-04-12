from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.default.Menu import menu_keys
from data.config import ADMINS
from filters import IsPrivate, IsGroup, AdminFilter
from keyboards.default.group_menu import group_menu

@dp.message_handler(IsPrivate(), CommandHelp(), chat_id=ADMINS)
async def hel(message: types.Message):
    await message.answer("Yes my Owner", reply_markup=menu_keys)

@dp.message_handler(IsPrivate(), CommandHelp())
async def hel(message: types.Message):
    await message.answer("Tell me what to do!", reply_markup=menu_keys)

@dp.message_handler(IsGroup(), CommandHelp() , AdminFilter())
async def menu(message: types.Message):
    await message.answer("Yes sir!", reply_markup=group_menu)
