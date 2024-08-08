from aiogram import types
import logging
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, echo, game
from db import db_main

admin = [668334970]


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='bot on')
        await db_main.sql_create()


async def on_shutdown(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='bot off')


commands.register_commands(dp)
game.register_quiz(dp)
echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
