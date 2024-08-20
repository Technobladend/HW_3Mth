# from aiogram import types
import logging
from config import dp, bot, admin
from aiogram.utils import executor
from handlers import commands, echo, game, FSM_reg, FSM_store, send_products, webapp, pin_message, admin_bot
from db import db_main


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='bot on')
        await db_main.sql_create()


async def on_shutdown(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='bot off')


commands.register_commands(dp)
game.register_quiz(dp)
FSM_reg.register_fsm_store(dp)
FSM_store.store_fsm(dp)
send_products.register_send_products_handler(dp)
webapp.register_webapp(dp)
pin_message.register_pin(dp)
admin_bot.register_admin(dp)
echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
