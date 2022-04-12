from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Let me do my job!"),
            types.BotCommand("help", "Tell me what to do!"),
            types.BotCommand("frr", "ghffghfgh")
        ]
    )
