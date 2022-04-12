from keyboards.inline.anonim_inline import qwerty
from aiogram import types
from loader import dp, bot
from aiogram.types import ReplyKeyboardMarkup
from states.anonim_state import anonim
from aiogram.dispatcher import FSMContext
from filters import IsPrivate


@dp.message_handler(IsPrivate(), text="Anonim message")
async def ano(message: types.Message):
    await message.reply("Write your message!")
    await anonim.answer.set()

@dp.message_handler(state=anonim.answer)
async def mes(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    category = await qwerty(user_id)
    await bot.send_message(chat_id=386029439, text=message.text, reply_markup=category)
    await message.answer("Your message was sent!")
    await state.finish()

@dp.callback_query_handler(lambda c: "answer" in c.data, state="*")
async def call(callback: types.CallbackQuery, state: FSMContext):
    a, user_id = callback.data.split(" ")
    async with state.proxy() as data:
        data["user_id"] = user_id
    await bot.send_message(chat_id=callback.from_user.id, text="Enter your answer!")
    await anonim.answer1.set()

@dp.message_handler(state=anonim.answer1)
async def mm(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["answer"] = message.text
    await bot.send_message(chat_id=data["user_id"], text=data["answer"])
    await state.finish()










