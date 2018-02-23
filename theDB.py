import sqlite3
from textFiles import textFilez
import csv
from dicts import items_dict
# from ui import add_items

def setup_db():


    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()

    try:
        c.execute('PRAGMA foreign_keys=ON')
        c.execute('CREATE TABLE IF NOT EXISTS items (indx INTEGER PRIMARY KEY AUTOINCREMENT, itemID INTEGER, itemName TEXT, itemPrice DECIMAL);')
        # c.execute('CREATE TABLE IF NOT EXISTS items(indx INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, itemID INTEGER NOT NULL AUTOINCREMENT, FOREIGN KEY (itemID) REFERENCES saleItems (itemID), itemName TEXT, itemPrice DECIMAL, FOREIGN KEY (itemPrice) REFERENCES saleItems (saleItemPriceEach));')
        # c.execute('CREATE TABLE IF NOT EXISTS saleItems(indx INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, saleID INTEGER NOT NULL AUTOINCREMENT, itemID INTEGER, FOREIGN KEY (itemID) REFERENCES items (itemID), saleItemQty INTEGER, saleItemPriceEach DECIMAL, FOREIGN KEY (saleItemPriceEach) REFERENCES items (itemPrice), saleItemTotal DECIMAL, saleDate VARCHAR(10));')
        c.execute('CREATE TABLE IF NOT EXISTS saleItems(indx INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, saleID INTEGER NOT NULL, itemID INTEGER, saleItemQty INTEGER, saleItemPriceEach DECIMAL, saleItemTotal DECIMAL, saleDate TEXT, FOREIGN KEY (itemID) REFERENCES items (itemID), FOREIGN KEY (saleItemPriceEach) REFERENCES items (itemPrice));')
        db.commit()

    except sqlite3.Error as err:
        print('{} = ERROR'.format(err))

    try:
        for item in items_dict:
            c.execute('INSERT OR REPLACE INTO items(indx, itemID, itemName, itemPrice) VALUES (null,?,?,?)', [items_dict['index'],items_dict['itemID'], items_dict['itemName'], items_dict['itemPrice']])
        db.commit()
        # data = textFilez.read_from_item_file_to_db()
        # print(data)

    except sqlite3.Error as err:
        print('{} = ERROR2'.format(err))

# def add_item_to_db(itemName, itemPrice):
#     db_filename  = "RMmgr_db.db"
#     db = sqlite3.connect(db_filename)
#     c = db.cursor()
#     c.execute('INSERT OR REPLACE INTO items(itemName, itemPrice) VALUES (null,null,?,?);', (itemName,itemPrice)


def main():
    setup_db()
    # add_item_to_db()

if __name__ == main():
    main()
