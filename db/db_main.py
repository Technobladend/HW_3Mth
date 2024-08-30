import sqlite3 as sq
from homework_3month.db import quaries
db = sq.connect('db/db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных sql3lite подключенна")
    cursor.execute(quaries.CREATE_TABLE_REGISTRATION)
    db.commit()


async def sql_insert_registration(firstname):
    cursor.execute(quaries.INSERT_INTO_TABLE_REGISTRATION, (
        firstname)
                   )
    db.commit()


async def sql_create_store():
    if db:
        print("1ая часть подключена")
    cursor.execute(quaries.CREATE_TABLE_PRODUCTS)
    cursor.execute(quaries.CREATE_TABLE_PRODUCT_DETAILS)
    cursor.execute(quaries.CREATE_TABLE_COLLECTION_PRODUCTS)
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


async def sql_insert_product_details(id_product, category, info_product):
    cursor.execute(quaries.INSERT_PRODUCT_DEATILS, (
        id_product,
        category,
        info_product
    )
                   )
    db.commit()


async def sql_insert_collection_products(product_id, collection_product):
    cursor.execute(quaries.INSERT_COLLECTION_PRODUCTS, (
        product_id,
        collection_product
    ))
    db.commit()
