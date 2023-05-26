import sqlite3 as sl

"""
SELECT ('столбцы или * для выбора всех столбцов; обязательно')
FROM ('таблица; обязательно')
WHERE ('условие/фильтрация, например, city = 'Moscow'; необязательно')
GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
"""

con = sl.connect('DARASTOCK.db', check_same_thread=False)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Stock (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            coordinates REAL);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER,
            name TEXT,
            count INTEGER,
            characteristic TEXT,
            picture BLOB,
            shelf_line DATETIME,
            day_in DATETIME
            stock_id INTEGER);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS CategoryOfProduct (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description INTEGER);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS OrderProduct (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            count INTEGER ,
            order_id INTEGER);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            data DATETIME,
            user_id INTEGER);
    """)
with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            number_phone INTEGER,
            passport TEXT);
    """)

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Relocation (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             from_stock_id INTEGER,
             product_id INTEGER,
             count INTEGER,
             where_stock_id INTEGER);
    """)

def show_category():
    '''
    :return: список категорий
    '''
    try:
        with con:
            data = con.execute(f"SELECT name FROM CategoryOfProduct")
            data = data.fetchall()
            list_cat = []
            for i in data:
                list_cat.append(i[0])
        return list_cat
    except Exception as e:
        print(e)
# print(show_category())

def show_products(cat_name):
    '''
    param название категорий
    :return: список продуктов
    '''
    try:
        with con:
            data = con.execute(f'''SELECT Products.name FROM Products
                                    JOIN CategoryOfProduct ON
                                    Products.category_id = CategoryOfProduct.id
                                    WHERE CategoryOfProduct.name = "{cat_name}" ''')
            data = data.fetchall()
            list_cat = []
            for i in data:
                list_cat.append(i[0])
        return list_cat
    except Exception as e:
        print(e)
# print(show_products("Мебель"))

def add_product_to_orser(order_id,name_product,count):
    '''
    :param order_id: номер заказа
    name_product имя товара
    count количество товара
    :return: добавление в заказ продуктов
    '''
    try:
        with con:
            data = con.execute(f'''SELECT id FROM ProductsWHERE Products.name = "{name_product}" ''')
            data = data.fetchall()
            id_pr = data[0][0]
    except Exception as e:
        return e
    try:
        sql_insert = f"INSERT INTO OrderProduct (order_id,product_id,count) values(?,?,?)"
        with con:
            con.execute(sql_insert, (order_id,id_pr,count))
        return True
    except Exception as e:
        return e
# print(add_product_to_orser("1","Диван","3"))

def registr_new_stock(name,address):
    '''
    :param name: название склада и адресс склада
    :param address:
    :return: новый зарегистрированный склад
    '''
    try:
        sql_insert = f"INSERT INTO Stock (name,address) values(?,?)"
        with con:
            con.execute(sql_insert, (name, address))
        return True
    except Exception as e:
        return e
# print(registr_new_stock("СКЛАД1","Минск,Центральная 8"))

def plus_product(name,count):
    '''
    :param name: имя товара и колличество
    :return: увеличение кол-ва товара
    '''
    try:
        nm = f"UPDATE Products SET count = count + {count} WHERE name = '{name}' "
        with con:
            con.execute(nm)
    except Exception as e:
        print("Ошибка: ", e)
# print(plus_product("Диван","3"))

def delete_product(name_product):
    '''
    :param name_product: имя проодукта
    :return: удалении этого продукта
    '''
    try:
        nm = f"DELETE FROM Products WHERE name = '{name_product}'"
        with con:
            con.execute(nm)
        return True
    except Exception as e:
        print("Ошибка: ", e)
# print(delete_product("Лампочка"))

def add_category(name,descriprion):
    try:
        sql_insert = f"INSERT INTO CategoryOfProduct (name,description) values(?,?)"
        with con:
            con.execute(sql_insert, (name, descriprion))
        return True
    except Exception as e:
        return e
# print(add_category("Обои","Красиво"))

def add_order(user_id):
    try:
        sql_insert = f"INSERT INTO Users (name,description) values(?,?)"
        with con:
            con.execute(sql_insert, (name, descriprion))
        return True
    except Exception as e:
        return e