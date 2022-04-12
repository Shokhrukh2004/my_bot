from aiogram import types
from loader import dp, bot
from data.config import CHANNELS
from utils.misc.follow import check
from keyboards.inline.chanel_inline import channel_inline

@dp.message_handler(commands=["start", "help"])
async def checker(message: types.Message):
    channel_format = ""
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channel_format += f"👉 <a href='{invite_link}'>{chat.title}</a>"
    await message.answer(f"In order to use the bot follow: \n{channel_format}", reply_markup=channel_inline,
                         disable_web_page_preview=True)

@dp.callback_query_handler(text="channel")
async def final(callback: types.CallbackQuery):
    result = ""
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        status = await check(user_id=callback.from_user.id, channel=channel)
        if not status:
            invite_link = await chat.export_invite_link()
            result += f"You are not follower.\n Follow {chat.title}\n 👉<a href='{invite_link}'>{chat.title}</a>"
        else:
            result += f"You have followed the {chat.title}"

    await callback.message.answer(result, disable_web_page_preview=True)







