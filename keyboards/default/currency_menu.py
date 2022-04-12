from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

curr_ency = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('USD  -----> UZS'),
            KeyboardButton('Wider Check!')
        ],
        [
            KeyboardButton('Ortga Qaytish!'),
            KeyboardButton('Go back!')
        ]
    ],
    resize_keyboard=True
)