from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

group_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("!Ban members"),
            KeyboardButton("!Unban members")
        ],
        [
            KeyboardButton("!Reading mode"),
            KeyboardButton("!Unread mode")
        ],
        [
            KeyboardButton("!Change photo"),
            KeyboardButton("!Change name"),
            KeyboardButton("!Change quote")
        ]
    ],
    resize_keyboard=True
)