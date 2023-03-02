import logging

from aiogram import types
from constant import get_welcome_message, create
from loader import dispatcher, bot
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.replay_markup_button import make_button


@dispatcher.message_handler(CommandStart())
async def start_bot(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_animation(
        chat_id=chat_id,
        animation="https://t.me/sinovuchun4101/15",
        caption=get_welcome_message(message.from_user.full_name),
        reply_markup=make_button(words=[create], row_width=2)
    )
