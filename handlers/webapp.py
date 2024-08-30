from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from homework_3month.config import dp


async def webapp_inline_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    geeks_online = InlineKeyboardButton(text="Geeks Online",
                                        web_app=types.WebAppInfo(url="https://online.geeks.kg"))
    kaktus_media = InlineKeyboardButton(text="kaktus media",
                                        web_app=types.WebAppInfo(url="https://kaktus.media"))
    netflix = InlineKeyboardButton(text='netflix',
                                   web_app=types.WebAppInfo(url="https://www.netflix.com"))
    jut_su = InlineKeyboardButton(text='jut-su',
                                  web_app=types.WebAppInfo(url='https://jut.su/.html'))
    spotify = InlineKeyboardButton(text='spotify',
                                   web_app=types.WebAppInfo(url="https://open.spotify.com"))

    keyboard.add(geeks_online, kaktus_media, netflix, jut_su, spotify)

    await message.answer(text="Нажми на кнопки для открытия сайтов", reply_markup=keyboard)


def register_webapp(dispatcher: Dispatcher):
    dp.register_message_handler(webapp_inline_button, commands=['webapp'])
