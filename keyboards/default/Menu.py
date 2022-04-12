from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_keys = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Bot info'),
            KeyboardButton('My info'),
            KeyboardButton('Search Wikipedia'),
            KeyboardButton('Check the Currency')
        ],
        [
#            KeyboardButton("Games --- O'yinlar"),
            KeyboardButton("Books --- Kitoblar"),
            KeyboardButton("Download google photo"),
#            KeyboardButton("Music vk"),
#            KeyboardButton("Movie search --- Kino qidirish")
        ],
        [
            KeyboardButton("Search item --- Umumiy qidirish"),
            KeyboardButton("Anonim message")
        ]
    ],
    resize_keyboard=True
)