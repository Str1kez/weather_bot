from aiogram.dispatcher.filters.state import StatesGroup, State


class Contact(StatesGroup):
    name = State()
    email = State()
    phone = State()
