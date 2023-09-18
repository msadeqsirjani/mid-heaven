from aiogram.dispatcher.filters.state import StatesGroup, State


class QuestionnairesState(StatesGroup):
    rendering_mode = State()
    style = State()
    number_of_storey = State()
    roof_type = State()
    number_of_material = State()
    garage = State()
    roof_type_advanced = State()
    details = State()
    overhang = State()
    style_advanced = State()
    num_of_outputs = State()
