from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bookss = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Math", callback_data="math"),
            InlineKeyboardButton(text="Read Books", callback_data="read_books")
        ],
        [
            InlineKeyboardButton(text="SAT Books", callback_data="sat"),
            InlineKeyboardButton(text="Programming Books", callback_data="programming")
        ],
        [
            InlineKeyboardButton(text="Historical Books", callback_data="history"),
            InlineKeyboardButton(text="Scary Books", callback_data="scary")
        ]
    ]
)

