from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BotInfo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Bot Haqida Malumot'),
            KeyboardButton('Info about Bot')
        ],
[
            KeyboardButton("Bot boshqaruvchi bilan bog'lanish!"),
            KeyboardButton("Approach the bot owner!")
        ],
        [
            KeyboardButton('Ortga Qaytish!'),
            KeyboardButton('Go back!')
        ]
    ],
    resize_keyboard=True
)