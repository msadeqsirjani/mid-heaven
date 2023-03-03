from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.replay_markup_button import make_button
from loader import dispatcher
from constant import create, cancel


@dispatcher.message_handler(Text(contains='cancel'), state="*")
async def cancel_bot(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Good. We will go back.", reply_markup=make_button(words=[create], row_width=2))
