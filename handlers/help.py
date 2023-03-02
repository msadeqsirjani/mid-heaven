from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dispatcher


@dispatcher.message_handler(CommandHelp())
async def help_bot(message: types.Message):
    text = ("Mid-Heaven: ",
            "/start - Launch the bot",
            "/help - Help",
            "/create - Create an image",
            "/cancel - Cancel running execution",
            )
    await message.answer('\n'.join(text))
