from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateImageState(StatesGroup):
    create_image = State()
