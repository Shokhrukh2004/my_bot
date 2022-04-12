from aiogram import types
from aiogram.dispatcher.filters.builtin import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        admin = await message.chat.get_member(message.from_user.id)
        return admin.is_chat_admin()