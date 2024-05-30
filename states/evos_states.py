from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Evos_States(StatesGroup):
    products_state = State()
