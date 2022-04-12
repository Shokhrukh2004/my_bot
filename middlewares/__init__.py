
from loader import dp
from . throttling import ThrottlingMiddleware
from . start_handler import Middlewares

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Middlewares())