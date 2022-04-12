from aiogram import types
from loader import dp
from filters import IsGroup

@dp.message_handler(IsGroup, content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new(message: types.Message):
    members = " ".join(m.get_mention(as_html=True) for m in message.new_chat_members)
    add = message.from_user.get_mention(as_html=True)
    await message.reply(f"Welcome dear {members}")
    await message.reply(f"{members.title()} you were added by {add}")
