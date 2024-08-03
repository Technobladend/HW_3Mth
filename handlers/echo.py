from aiogram import types, Dispatcher


async def echo_handler(message: types.Message) -> None:
    if message.text.isdigit():
        arg = int(message.text)
        await message.reply(arg ** 2)
    else:
        await message.reply(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)

