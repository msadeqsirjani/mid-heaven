from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dispatcher, bot
from constant import create, create_image, create_description, errors, block, prepare_example_caption
from states.create_image_state import CreateImageState
from states.questionnaires_state import QuestionnairesState
from keyboards.replay_markup_button import make_button
from utilities.midjourney import draw_picture
from utilities.promt_generator import generate


@dispatcher.message_handler(text=create, state='*')
async def help_bot(message: types.Message, state: FSMContext):
    await CreateImageState.create_image.set()
    await state.reset_state(with_data=True)
    await message.answer(text=create_description, reply_markup=make_button(words=["Start Poll"], row_width=2))
    user = message.from_user


@dispatcher.message_handler(Text(equals="Start Poll", ignore_case=True))
async def ask_rendering_mode(message: types.Message):
    await message.answer("Rendering Mode?",
                         reply_markup=make_button(words=["Realistic Rendering", "Black / White"], row_width=2))
    await QuestionnairesState.rendering_mode.set()


@dispatcher.message_handler(state=QuestionnairesState.rendering_mode)
async def answer_rendering_mode(message: types.Message, state: FSMContext):
    await state.update_data(rendering_mode=f"Rendering Mode: {message.text}")
    await message.answer("Style?",
                         reply_markup=make_button(words=["Traditional Style", "Modern Style", "Futuristic"],
                                                  row_width=2))
    await QuestionnairesState.style.set()


@dispatcher.message_handler(state=QuestionnairesState.style)
async def answer_style(message: types.Message, state: FSMContext):
    await state.update_data(style=f"Style: {message.text}")
    await message.answer("Number of Storey?",
                         reply_markup=make_button(words=["One Floor", "Two Floor"], row_width=2))
    await QuestionnairesState.number_of_storey.set()


@dispatcher.message_handler(state=QuestionnairesState.number_of_storey)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(number_of_storey=f"Number of Storey: {message.text}")
    await message.answer("Roof Types?",
                         reply_markup=make_button(
                             words=["Flat Roof", "Low-pitched Roof", "Moderate Pitched Roof", "Steep-pitched Roof"],
                             row_width=2))
    await QuestionnairesState.roof_type.set()


@dispatcher.message_handler(state=QuestionnairesState.roof_type)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(roof_type=f"Roof Type: {message.text}")
    await message.answer("Number of Materials?", reply_markup=make_button(words=["1", "2", "3"], row_width=2))
    await QuestionnairesState.number_of_material.set()


@dispatcher.message_handler(state=QuestionnairesState.number_of_material)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(number_of_material=f"Number Of Materials: {message.text}")
    await message.answer("Garage?", reply_markup=make_button(words=["No Garage", "1 Garage", "2 Garage"], row_width=2))
    await QuestionnairesState.garage.set()


@dispatcher.message_handler(state=QuestionnairesState.garage)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(garage=f"Garage: {message.text}")
    await message.answer("Roof Type (advanced)?",
                         reply_markup=make_button(
                             words=["Gable Roof", "Cross Gable Roof", "Mansard Roof", "Hip Roof", "Saltbox Roof",
                                    "Gambler Roof", "Shed Roof", "Roof Extends to the ground"], row_width=2))
    await QuestionnairesState.roof_type_advanced.set()


@dispatcher.message_handler(state=QuestionnairesState.roof_type_advanced)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(garage=f"Roof Type (advanced): {message.text}")
    await message.answer("Details?", reply_markup=make_button(words=["Dormers", "Tiled Roof"], row_width=2))
    await QuestionnairesState.details.set()


@dispatcher.message_handler(state=QuestionnairesState.details)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(garage=f"Details: {message.text}")
    await message.answer("Overhangs?",
                         reply_markup=make_button(words=["No Overhangs", "Roof Overhang", "Flared eaves"], row_width=2))
    await QuestionnairesState.overhang.set()


@dispatcher.message_handler(state=QuestionnairesState.overhang)
async def answer_number_of_storey(message: types.Message, state: FSMContext):
    await state.update_data(garage=f"Overhangs: {message.text}")
    await message.answer("Style (advanced)?",
                         reply_markup=make_button(
                             words=["Modern Style", "Traditional Style", "Shed Style", "Queen Anne Style",
                                    "Georgian Style", "Greek Revival Style", "Spanish Revival Style", ], row_width=2))
    await QuestionnairesState.style_advanced.set()


@dispatcher.message_handler(state=QuestionnairesState.style_advanced)
async def echo_bot(message: types.Message, state: FSMContext):
    await state.update_data(garage=f"Style (advanced): {message.text}")
    await CreateImageState.create_image.set()

    chat_id = message.from_user.id
    user_data = await state.get_data()

    print(user_data)

    original_prompt = generate(user_data)
    prompt = f"mdjrny-v4 style {original_prompt.lower().strip()}"

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
