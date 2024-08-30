from aiogram import types, Dispatcher
from homework_3month.config import bot, admin


async def pin_message(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.answer(text='Только админ может закреплять сообщения')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
            await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
    else:
        await message.answer('Эта команда должна быть использована в группе')


async def unpin_message(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.answer(text="Только админ может откреплять")
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
            # try:
            await bot.unpin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
            await message.answer(text='Открепленно')
            # except Exception as e:
            #     await message.answer(f'не удалось отправить сообщение {e}')
    else:
        await message.answer('команда рабоатет онли в группе')


def register_pin(dispatcher: Dispatcher):
    dispatcher.register_message_handler(pin_message, text=['!pin'])
    dispatcher.register_message_handler(unpin_message, text=['!unpin'])
