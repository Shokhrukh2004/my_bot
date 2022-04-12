from aiogram import types
from loader import dp
import requests
from aiogram.types import ReplyKeyboardRemove
API = 'https://v6.exchangerate-api.com/v6/c774b6c2935ee332e2c4c069/pair/USD/UZS'
responce = requests.get(API)
sotish = responce.json()

API2 = 'https://v6.exchangerate-api.com/v6/c774b6c2935ee332e2c4c069/latest/USD'
response2 = requests.get(API2)
general = response2.json()


@dp.message_handler(text='USD  -----> UZS')
async def currency(message: types.Message):
    a = sotish['conversion_rate']
    await message.answer(f"Today's currency (USD --> UZS) : {a}", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Wider Check!')
async def wider(message: types.Message):
    await message.answer("World's all currencies to UZS:", reply_markup=ReplyKeyboardRemove())
    a = general['conversion_rates']
    await message.answer(a)


