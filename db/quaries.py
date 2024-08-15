CREATE_TABLE_REGISTRATION = """
    CREATE TABLE IF NOT EXISTS registration
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id VARCHAR(255),
    firstname VARCHAR(255)
    )
"""

INSERT_INTO_TABLE_REGISTRATION = """
    INSERT INTO registration(telegram_id, firstname)
    VALUES(?, ?)
"""


CREATE_TABLE_PRODUCTS = """
CREATE TABLE IF NOT EXISTS product
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (255),
size VARCHAR (255),
price VARCHAR (255),
product_id VARCHAR(255),
photo TEXT
)
"""

INSERT_PRODUCTS = """
INSERT INTO product(name, size, price, product_id, photo)
VALUES(?, ?, ?, ?, ?)
"""

CREATE_TABLE_PRODUCT_DETAILS = """
CREATE TABLE IF NOT EXISTS product_details
(id INTEGER PRIMARY KEY AUTOINCREMENT,
id_product VARCHAR(255),
category VARCHAR(255),
info_product VARCHAR(255)
)
"""

INSERT_PRODUCT_DEATILS = """
INSERT INTO product_details(id_product, category, info_product)
VALUES (?, ?, ?)
"""





