from aiogram import types, Dispatcher
from homework_3month.config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz(message: types.Message):
    button_quiz = InlineKeyboardMarkup(row_width=1)

    button_quiz.add(InlineKeyboardButton("Дальше!", callback_data="button_1"))

    question = 'Dark souls or casual'

    answer = ['Dark souls:3', 'casual;/', 'fear and hunger(wtf)']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='eblan suka tupoi',
        open_period=60,
        reply_markup=button_quiz

    )


async def quiz_2(call: types.CallbackQuery):
    button_quiz = InlineKeyboardMarkup(row_width=1)

    button_quiz.add(InlineKeyboardButton("Дальше!", callback_data="button_2"))

    question = 'Best game in universe'

    answer = ['CS 2', 'DOTA 2', 'Valorant', 'Fortnite', 'Dark souls', 'bloodborne', 'minecraft']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=4,
        explanation='ОЙОЙОЙ ПИДАРААААЗ',
        open_period=60,
        reply_markup=button_quiz

    )


async def quiz_3(call: types.CallbackQuery):
    button_quiz = InlineKeyboardMarkup(row_width=1)

    button_quiz.add(InlineKeyboardButton("Дальше!", callback_data="button_3"))

    question = 'Best album of all time'

    answer = ['the great dismal', 'the wall', 'dont mind the bollocks its sex pistols', 'recovery']

    await bot.send_photo(chat_id=call.from_user.id,
                         photo='https://npr.brightspotcdn.com/legacy/wp-content/uploads/gallery-221013-mini-1.jpg')

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='naaah',
        open_period=60,
        reply_markup=button_quiz

    )


async def quiz_4(call: types.CallbackQuery):

    question = 'do u wanna play game?'

    answer = ['yes sir', 'yeah', 'YASSS SLAAY', 'naaah bro']

    await bot.send_photo(chat_id=call.from_user.id,
                         photo='https://qph.cf2.quoracdn.net/main-qimg-38cc761ac297cfb5cad09b6ba7b24980-lq')

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation='теперь пропиши /game',
        open_period=60

    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(quiz_3, text='button_2')
    dp.register_callback_query_handler(quiz_4, text='button_3')
