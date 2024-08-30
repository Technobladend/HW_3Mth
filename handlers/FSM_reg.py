import re
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import homework_3month.buttons as buttons
from homework_3month.Google_sheets.sheets import update_google_sheet_register, open_sheet


class FSM_reg(StatesGroup):
    full_name = State()
    age = State()
    email = State()
    gender = State()
    phone = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message, state: FSMContext):
    row = open_sheet()

    await message.answer(text="Привет!\n"
                              "Давай знакомиться, как тебя зовут?\n"
                              "\nЧто бы воспользоваться командами, нажми на 'Отмена' \n\n"
                              "Укажите своё ФИО:", reply_markup=buttons.cancel)
        
    await FSM_reg.full_name.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text

    await FSM_reg.next()
    await message.answer(text="Укажи свой возраст:")


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await FSM_reg.next()
    await message.answer(text="Укажи свою почту:")


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        email = message.text.strip()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            await message.answer(text='Некорректный формат электронной почты!')
            return
        data['email'] = email

    await FSM_reg.next()
    await message.answer(text="Укажи свой гендер:")


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await FSM_reg.next()
    await message.answer(text="Отправь свой номер:")


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    await FSM_reg.next()
    await message.answer(text="Отправь свою фотку:")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption=f"Ваше ФИО - {data['full_name']}\n"
                               f"Возраст - {data['age']}\n"
                               f"Почта - {data['email']}\n"
                               f"Пол - {data['gender']}\n"
                               f"Номер телефона - {data['phone']}\n"
                               f"Верны ли данные?",
                               reply_markup=buttons.yes_no
                               )
    await FSM_reg.next()


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        kb = types.ReplyKeyboardRemove()

        async with state.proxy() as data:
            name = data['full_name']
            age = data['age']
            email = data['email']
            gender = data['gender']
            phone = data['phone']

            update_google_sheet_register(name=name,
                                         age=age,
                                         email=email,
                                         gender=gender,
                                         phone=phone)

        await message.answer(text='Данные сохранены!', reply_markup=kb)
        await state.finish()

    else:
        await message.answer(text='Регистрация отменена')
        await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено!')


def register_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True
                                                 ), state="*")
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSM_reg.full_name)
    dp.register_message_handler(load_age, state=FSM_reg.age)
    dp.register_message_handler(load_email, state=FSM_reg.email)
    dp.register_message_handler(load_gender, state=FSM_reg.gender)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)
    dp.register_message_handler(load_photo, state=FSM_reg.photo,
                                content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_reg.submit)
