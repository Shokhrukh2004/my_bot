from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.misc import follow
from loader import bot


class Middlewares(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        final_status = True
        user = update.message.from_user.id
        result = "In order to run our bot follow:\n"
        for channel in CHANNELS:
            status = await follow.check(user_id=user, channel=channel)
            final_status *= status
            chat = await bot.get_chat(channel)
            if not status:
                invite_link = await chat.export_invite_link()
                result += f"<a href='{invite_link}'>{chat.title}</a>"
        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True)
            raise CancelHandler()




