from aiogram import types
from loader import dp, bot
from filters import IsGroup

@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def left(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        member = message.left_chat_member.get_mention(as_html=True)
        await message.answer(f"{member.title()} left the group!")

    elif message.left_chat_member.id == (await bot.me).id:
        await message.answer(f"i kicked {message.left_chat_member.get_mention(as_html=True).title()}!")

    else:
        kicker = message.from_user.get_mention(as_html=True)
        kicked = message.left_chat_member.get_mention(as_html=True)
        await message.answer(f"{kicked.title()} was kicked out by {kicker.title()}!")


