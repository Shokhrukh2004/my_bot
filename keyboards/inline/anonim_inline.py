from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def qwerty(id):
    anonim = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Answer", callback_data=f"answer {id}")
            ]
        ]
    )
    return anonim



