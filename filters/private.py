from aiogram import types
from aiogram.dispatcher.filters.builtin import BoundFilter

class IsPrivate(BoundFilter):
    async def check(self, messaege: types.Message) -> bool:
        return messaege.chat.type == types.ChatType.PRIVATE
