from aiogram import types, Dispatcher
from config import bot
import os
from aiogram.types import InputFile
import random


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


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands="start")
    dp.register_message_handler(info_handler, commands="info")
    dp.register_message_handler(mem_handler, text='send tool meme')
    dp.register_message_handler(lyrics_handler, text="send deftones lyrics")
