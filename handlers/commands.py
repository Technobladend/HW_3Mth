from aiogram import types, Dispatcher
from homework_3month.config import bot
import os
from aiogram.types import InputFile
import random
import time


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать!')


async def info_handler(message: types.Message):
    await message.answer('Просто бот для домашки')


async def mem_handler(message: types.Message):
    path = 'media_1/'
    files = []

    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)

    random_photo = random.choice(files)

    await message.answer_photo(photo=InputFile(random_photo))


async def lyrics_handler(message: types.Message):
    path = 'phrases/'
    files = []
    for f in os.listdir(path):
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path):
            files.append(full_path)

    random_phrase = random.choice(files)

    await message.answer_document(document=InputFile(random_phrase))


async def game_dice(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Игра начинается...'
                                                              '\nПервым кидает бот, потом ваш ход')
    dices = ['🎳’', '🎲', '🎯']

    dice_1 = await bot.send_dice(message.from_user.id, emoji=random.choice(dices))
    value1 = dice_1.dice.value
    time.sleep(3)

    dice_2 = await bot.send_dice(message.from_user.id, emoji=random.choice(dices))
    value2 = dice_2.dice.value
    time.sleep(5)

    if value1 > value2:
        await bot.send_message(message.from_user.id, "Бот выиграл, лол")
    elif value1 < value2:
        await bot.send_message(message.from_user.id, "Удивительно, вы выиграли...")
    else:
        await bot.send_message(message.from_user.id, "Ничья")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands="start")
    dp.register_message_handler(info_handler, commands="info")
    dp.register_message_handler(mem_handler, text='send tool meme')
    dp.register_message_handler(lyrics_handler, text="send deftones lyrics")
    dp.register_message_handler(game_dice, commands="game")
