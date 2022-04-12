from aiogram import types
from loader import dp
from states.wiki_state import wiki
import wikipedia
from aiogram.dispatcher import FSMContext

@dp.message_handler(text='Uzbek tilida')
async def uzbek_wiki(message: types.Message):
    wikipedia.set_lang('uz')
    await wiki.wiki.set()
    await message.answer('Mavzuni kiriting!')

@dp.message_handler(state=wiki.wiki)
async def wiki_2(message: types.Message, state=FSMContext):
    try:
        product = wikipedia.summary(message.text)

    except:
        await message.answer(f'Kechirasiz {message.from_user.first_name.title()} mavzuga oid wikipedia topilmadi!')
        await state.finish()
    else:
        await message.answer(product)
        await state.finish()


@dp.message_handler(text='Search in English')
async def eng_wiki(message: types.Message):
    wikipedia.set_lang('en')
    await wiki.wiki.set()
    await message.answer('Enter the topic! ')

@dp.message_handler(state=wiki.wiki)
async def wiki_2(message: types.Message, state=FSMContext):
    try:
        product = wikipedia.summary(message.text)
    except:
        await message.answer(f'Sorry {message.from_user.first_name.title()}, there is no such a wikipedia!🥺')
        await state.finish()
    else:
        await message.answer(product)
        await state.finish()









