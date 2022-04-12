from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channel_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Check your follow!", callback_data="channel")
        ]
    ]
)