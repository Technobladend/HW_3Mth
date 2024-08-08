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
