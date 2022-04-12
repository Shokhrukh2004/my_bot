from aiogram import types
from loader import dp

@dp.message_handler(text='My info')
async def user_info(message: types.Message):
    f_name = message.from_user.first_name
    l_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = message.from_user.id
    await message.answer(f"Name: {f_name}\n"
           f"Last name: {l_name}\n"
           f"Username: {username}\n"
           f"Chat ID: {chat_id}")
