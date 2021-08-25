from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import Contact
from loader import dp


@dp.message_handler(Command("send_contact"))
async def invite_to_send(message: types.Message):
    await message.answer("Введите свое Имя")
    await Contact.name.set()


@dp.message_handler(state=Contact.name)
async def enter_email(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Введите почту:")
    await Contact.email.set()


@dp.message_handler(state=Contact.email)
async def enter_phone(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите номер телефона")
    await Contact.phone.set()


@dp.message_handler(state=Contact.phone)
async def enter_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data["name"]
    email = data["email"]
    phone = message.text
    await message.answer("Спасибо\n"
                         "Вот ваши данные:\n"
                         f"<u>Имя</u>: {name}\n"
                         f"<u>Email</u>: {email}\n"
                         f"<u>Телефон</u>: {phone}")
    await state.reset_state()
