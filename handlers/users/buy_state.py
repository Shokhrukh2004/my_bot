from aiogram import types
from loader import dp
from states.buy_state import buy
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

@dp.message_handler(text="Search item --- Umumiy qidirish")
async def buys(message: types.Message):
    await message.answer(f"{message.from_user.first_name.title()} let me get info about item! ", reply_markup=ReplyKeyboardRemove())
    await message.answer("What is the name of the item?")
    await buy.name.set()

@dp.message_handler(state=buy.name)
async def names(message: types.Message, state=FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )

    await message.answer("What model?")
    await buy.next()

@dp.message_handler(state=buy.model)
async def modl(message: types.Message, state=FSMContext):
    model = message.text
    await state.update_data(
        {"model": model}
    )
    await message.answer("What color?")
    await buy.next()

@dp.message_handler(state=buy.color)
async def col(message: types.Message, state=FSMContext):
    color = message.text
    await state.update_data(
        {"color": color}
    )
    await message.answer("What condition?")
    await buy.next()

@dp.message_handler(state=buy.condition)
async def con(message: types.Message, state=FSMContext):
    condition = message.text
    await state.update_data(
        {"condition": condition}
    )
    await message.answer("Maximum cost?")
    await buy.next()

@dp.message_handler(state=buy.cost)
async def cos(message: types.Message, state=FSMContext):
    cost = message.text
    await state.update_data(
        {"cost": cost}
    )
    data = await state.get_data()
    name = data.get("name")
    model = data.get("model")
    color = data.get("color")
    condition = data.get("condition")
    cost = data.get("cost")
    await message.answer(f"I got following info:\n"
                         f"<b>Name</b>: {name.title()}\n"
                         f"<b>Model</b>: {model.title()}\n"
                         f"<b>Condition</b>: {condition.title()}\n"
                         f"<b>Color</b>: {color.title()}\n"
                         f"<b>Cost</b>: {cost.title()}")
    await message.answer(f"Thank you {message.from_user.first_name.title()}!")
    await state.finish()
