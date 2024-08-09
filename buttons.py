from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

size_variations = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('XS'), KeyboardButton('S'), KeyboardButton('M'), KeyboardButton('L'), KeyboardButton('XL')
)

yes_no = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Да'), KeyboardButton('Нет')
)