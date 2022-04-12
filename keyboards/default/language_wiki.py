from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lang_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Uzbek tilida'),
            KeyboardButton('Search in English')
        ],
        [
            KeyboardButton('Ortga Qaytish!'),
            KeyboardButton('Go back!')
        ]
    ],
    resize_keyboard=True
)