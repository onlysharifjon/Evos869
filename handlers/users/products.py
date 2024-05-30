from loader import dp
from states.evos_states import Evos_States
import sqlite3
from aiogram import types


def connector_database(product_name):
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    return cursor.execute('SELECT * FROM all_product WHERE name=?', (product_name,)).fetchone()


@dp.message_handler(state=Evos_States.products_state, content_types=types.ContentType.TEXT)
async def products_sender(message: types.Message):
    b = connector_database(message.text)
    await message.answer_photo(photo=open(b[1], 'rb'),caption=f'Narx: {b[3]}')

    # await message.answer(f'Siz {message.text} mahsulot tanladingiz')
