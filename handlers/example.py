import io
import os
from settings import BASE_DIR
from glob import glob
from aiogram import types
from aiogram.types.input_file import InputFile
from loader import dispatcher, bot
from constant import prepare_example_caption, create, null_description, description
from keyboards.replay_markup_button import make_button


@dispatcher.message_handler(commands=['example'])
async def example_bot(message: types.Message):
    try:
        chat_id = message.from_user.id
        example_photos = glob(f'{BASE_DIR}\\media\\*.*')
        for index, example_photo in enumerate(example_photos, start=1):
            await bot.send_photo(
                chat_id=chat_id,
                photo=InputFile(example_photo),
                caption=prepare_example_caption(description, index),
                reply_markup=make_button(
                    words=[create],
                    row_width=2
                )
            )
    except Exception as ex:
        print(ex)
        await message.answer(text=null_description)
