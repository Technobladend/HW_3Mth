from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons


class FSM_store(StatesGroup):
    product_name = State()
    size = State()
    category = State()
    price = State()
    product_photo = State()
    answer_from_user = State()


async def fsm_start(message: types.Message):
    await message.answer(text="Здравствуйте!\n"
                              "Укажите название товара:")
    await FSM_store.product_name.set()


async def load_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text

        await FSM_store.next()
        await message.answer(text="Укажите размер товара:", reply_markup=buttons.size_variations)


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

        kb = types.ReplyKeyboardRemove()

        await FSM_store.next()
        await message.answer(text="Укажите категорию товара:", reply_markup=kb)


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

        await FSM_store.next()
        await message.answer(text="Введите стоимость товара:")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

        await FSM_store.next()
        await message.answer(text="Отправьте фотографию товара:")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id

        await message.answer_photo(photo=data['product_photo'],
                                   caption=f"Название товара - {data['product_name']}\n"
                                           f"Размер - {data['size']}\n"
                                           f"Категория - {data['category']}\n"
                                           f"Цена товара - {data['price']}\n"
                                   )

        await FSM_store.next()
        await message.answer(text='Верны ли данные?', reply_markup=buttons.yes_no)


async def answer_from_user(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['answer_from_user'] = message.text
        kb = types.ReplyKeyboardRemove()
    if data['answer_from_user'] == 'Да':

        await message.answer(text='Данные сохранены', reply_markup=kb)
        await state.finish()
    elif data['answer_from_user'] == 'Нет':
        await message.answer(text='Отменено', reply_markup=kb)
        await state.finish()


def register_fsm_store(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['store'])
    dp.register_message_handler(load_product, state=FSM_store.product_name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.product_photo,
                                content_types=['photo'])
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(answer_from_user, state=FSM_store.answer_from_user)
