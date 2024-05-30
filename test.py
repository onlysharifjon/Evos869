import sqlite3

connect = sqlite3.connect('products.db')
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS all_product(name TEXT,photo TEXT,category TEXT,price INTEGER)')

cursor.execute('INSERT INTO all_product VALUES(?,?,?,?)',
               ('Combo Plus Isituvchan (Qora choy)', 'images/combo_plus_qorachoy.jpg', 'setlar',16000))
connect.commit()