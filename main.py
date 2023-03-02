from aiogram import executor
from loader import dispatcher as dp
from handlers import *
from errors import *
from utilities.commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher=dispatcher)


executor.start_polling(dp, on_startup=on_startup)
