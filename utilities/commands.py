from aiogram import types


async def set_default_commands(dispatcher):
    await dispatcher.bot.set_my_commands([
        types.BotCommand('start', 'Launch the bot'),
        types.BotCommand('help', 'Help'),
        types.BotCommand('create', 'Create an image'),
        types.BotCommand('cancel', 'Cancel running execution'),
        types.BotCommand('example', 'Show examples'),
    ])
