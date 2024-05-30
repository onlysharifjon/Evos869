from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📲Raqamingizni kiriting!', request_contact=True)
        ]
    ],
    resize_keyboard=True
)

asosiy_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🍴 Menyu")

        ],
        [
            KeyboardButton('📋 Mening buyurtmalarim')
        ],
        [
            KeyboardButton('📥 Savat'),
            KeyboardButton('📞 Aloqa')
        ],
        [
            KeyboardButton('📨 Xabar yuborish'),
            KeyboardButton('⚙️ Sozlamalar')
        ],
        [
            KeyboardButton('ℹ️ Biz haqimizda')
        ]

    ],
    resize_keyboard=True
)


menyu_part = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Setlar (8)')
        ],
        [
            KeyboardButton(text='Lavash (9)'),
            KeyboardButton(text='Shaurma (4)')
        ],
        [
            KeyboardButton(text='Burger (4)'),
            KeyboardButton(text='Hot-Dog (8)')
        ],
        [
            KeyboardButton("Ichimliklar (11)")
        ],
        [
            KeyboardButton('Shirinlik va disertlar (4)')
        ],
        [
            KeyboardButton('Garnirlar (10)')
        ],
        [
            KeyboardButton('🔙 Orqaga qaytish')
        ]
    ],
    resize_keyboard=True
)


setlar_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Combo Plus Isituvchan (Qora choy)"),
            KeyboardButton("FitCombo")
        ],
        [
            KeyboardButton("Iftar kofte grill mol go'shtidan"),
            KeyboardButton("Donar boks  mol go'shtidan")
        ],
        [
            KeyboardButton("Donar boks tovuq go'shtidan"),
            KeyboardButton("COMBO+")
        ],
        [
            KeyboardButton("Iftar strips tovuq go'shtidan"),
            KeyboardButton("Kids COMBO")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish"),
        ],
    ],
    resize_keyboard=True
)