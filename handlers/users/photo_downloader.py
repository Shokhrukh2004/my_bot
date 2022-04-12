from aiogram import types
from loader import dp
from states.photo_state import PhotoState
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="Download google photo")
async def down(message: types.Message):
    await message.answer("Paste the link! ")
    await PhotoState.photo.set()

@dp.message_handler(state=PhotoState.photo)
async def load(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(photo=message.text)
    except Exception:
        await message.answer(f"Sorry try again!")
    await state.finish()
    await message.delete()



