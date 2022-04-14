# from environs import Env

# # Теперь используем вместо библиотеки python-dotenv библиотеку environs
# env = Env()
# env.read_env()

# BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
# ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
# CHANNELS = ["@multi_bot_uzb"]
import os

ADMINS = list(os.environ.get("ADMINS"))
BOT_TOKEN=str(os.environ.get("BOT_TOKEN"))
CHANNELS=str(os.environ.get("CHANNELS"))
