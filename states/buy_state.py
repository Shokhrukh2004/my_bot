from aiogram.dispatcher.filters.state import State, StatesGroup

class buy(StatesGroup):
    name = State()
    model = State()
    color = State()
    condition = State()
    cost = State()
