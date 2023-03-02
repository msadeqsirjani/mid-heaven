from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dispatcher, bot
from constant import create, create_image, create_description, errors, block, prepare_example_caption
from states.create_image_state import CreateImageState
from keyboards.replay_markup_button import make_button
from utilities.midjourney import draw_picture


@dispatcher.message_handler(text=create)
async def help_bot(message: types.Message):
    await CreateImageState.create_image.set()
    await message.answer(text=create_description)


@dispatcher.message_handler(state=CreateImageState.create_image)
async def echo_bot(message: types.Message, state: FSMContext):
    await CreateImageState.create_image.set()

    chat_id = message.from_user.id
    original_prompt = message.text
    prompt = original_prompt.lower().strip()

    await message.answer(create_image)

    photo = draw_picture(prompt=prompt)[0]

    if photo:
        await bot.send_photo(chat_id=chat_id,
                             photo=photo,
                             caption=prepare_example_caption(original_prompt),
                             reply_markup=make_button(words=[create], row_width=2))
        await state.finish()
    else:
        await message.answer(text=errors)
    await state.finish()
