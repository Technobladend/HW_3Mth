from aiogram import types, Dispatcher
from config import admin, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging


async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f"Добро пожаловать, {member.full_name}\n\n"
                             f"Правила группы:\n"
                             f"* Не спамить\n"
                             f"* Не материться\n"
                             f"* Обсуждение политических тем\n")

# user_chances = {}
words = ['дурак', 'дебил', 'кретин', 'даун', 'амеба', 'израиль', 'украина', 'россия']


async def filter_word(message: types.Message):
    message_text = message.text.lower()
    # user_id = message.from_user.id

    for word in words:
        if word in message_text:
            await message.answer('Не ругайся!')
            await message.delete()
            # user_chances[user_id] += 1
            # if user_chances[user_id] == 3:
            #     await bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)
            #     await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)
            #     await message.answer(text='Пользователь был исключен')
            #     user_chances[user_id] = 0
            # return

    # user_chances[user_id] = 0


async def delete_user_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.answer('Чорт, ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name

            await message.answer(f'Вы действительно хотите удалить {user_name} ?',
                                    reply_markup=InlineKeyboardMarkup().add(
                                        InlineKeyboardButton(f'Удалить',
                                        callback_data=f'delete_user {user_id}')))

    else:
        await message.answer('Эта команда должна быть использована в группе')


async def complete_delete_user(call: types.CallbackQuery):
    user_id = int(call.data.replace("delete_user ", ""))
    from_user_id = call.from_user.id

    try:
        if from_user_id not in admin:
            await call.answer('Чорт, ты не админ!')
            return

        await bot.kick_chat_member(call.message.chat.id, user_id)
        await bot.unban_chat_member(call.message.chat.id, user_id)

        await call.answer(text='Пользователь удален!', show_alert=True)

        await bot.delete_messages(call.message.chat.id, call.message.message_id)

    except Exception as e:
        logging.error(f'Error in complete_delete_user: {e}')
        await call.answer(text='Не удалось удалить пользователя', show_alert=True)


user_warnings = {}


async def user_warning(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.reply("Ты не админ")
        elif not message.reply_to_message:
            await message.reply("Комадна должно быть ответом на сообщение:")
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

            for Admin in admin:
                await bot.send_message(chat_id=Admin,
                                       text=f"{user_name} получил предупреждение ({user_warnings[user_id]}/3)")

                if user_warnings[user_id] >= 3:
                    await bot.kick_chat_member(message.chat.id, user_id)
                    await bot.unban_chat_member(message.chat.id, user_id)

                    await bot.send_message(chat_id=message.chat.id,
                                           text=f"{user_name} был удален за превышение количества предупреждений!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(welcome_user,
                                content_types=[types.ContentType.NEW_CHAT_MEMBERS])
    dp.register_message_handler(delete_user_handler, commands=['delete'])
    dp.register_callback_query_handler(complete_delete_user,
                                       lambda call: call.data and call.data.startswith('delete_user '))
    dp.register_message_handler(user_warning, commands=['warn'])
    dp.register_message_handler(filter_word)
