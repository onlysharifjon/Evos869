from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from keyboards.default.start_buttons import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("<b>EVOS | Доставка</b> botiga xush kelibsiz!")
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki +998XX XXXXXXX ko'rinishida yozing.

https://evos.uz/uz/about/    
    ''', reply_markup=contact_button)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(message: types.Message):
    await message.reply(reply_markup=ReplyKeyboardRemove(), text='Telefon raqamingiz qabul qilindi✅')
    await message.answer('<b>🛒 Asosiy Menyu</b>')
    await message.answer('Marhamat buyurtma berishingiz mumkin!', reply_markup=asosiy_menyu)


# gitga push qilyapman

@dp.message_handler(text="🍴 Menyu")
async def menyu_uchun(message: types.Message):
    await message.answer('Menyulardan Birini tanlang !', reply_markup=menyu_part)

from states.evos_states import Evos_States
@dp.message_handler(text='Setlar (8)')
async def setlat_uchun(message: types.Message):
    await message.answer_photo(photo=open("images/setlar.png", 'rb'),reply_markup=setlar_menyu)
    await Evos_States.products_state.set()