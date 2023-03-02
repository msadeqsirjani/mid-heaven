from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from constant import cancel


def make_button(words: list, row_width: int = 1) -> ReplyKeyboardMarkup:
    button_groups = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=True)

    for word in words:
        if word is not None:
            button_groups.insert(KeyboardButton(text=word))

    return button_groups
