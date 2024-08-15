import sqlite3 as sq
from db import quaries
db = sq.connect('db/db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных sql3lite подключенна")
    cursor.execute(quaries.CREATE_TABLE_REGISTRATION)
    db.commit()


async def sql_insert_registration(telegram_id, firstname):
    cursor.execute(quaries.INSERT_INTO_TABLE_REGISTRATION, (
        telegram_id, firstname)
                   )
    db.commit()


async def sql_create_store():
    if db:
        print("1ая часть подключена")
    cursor.execute(quaries.CREATE_TABLE_PRODUCTS)
    db.commit()


async def sql_insert_products(name, size, price, product_id, photo):
    cursor.execute(quaries.INSERT_PRODUCTS, (
        name,
        size,
        price,
        product_id,
        photo
    ))

    db.commit()


async def sql_create_product_details():
    if db:
        print("2ая часть подключена")
    cursor.execute(quaries.CREATE_TABLE_PRODUCT_DETAILS)
    db.commit()


async def sql_insert_product_details(id_product, category, info_product):
    cursor.execute(quaries.INSERT_PRODUCT_DEATILS, (
        id_product,
        category,
        info_product
    )
                   )
    db.commit()
