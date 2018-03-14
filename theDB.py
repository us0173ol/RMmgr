import sqlite3
# from textFiles import textFilez
import csv
from dicts import *
# from ui import add_items

def setup_db():


    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()



    try:
        c.execute('PRAGMA foreign_keys=ON')
        # c.execute('DROP TABLE IF EXISTS items')
        c.execute('CREATE TABLE IF NOT EXISTS items (itemID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, itemName TEXT UNIQUE, itemPrice DECIMAL);')
        # c.execute('INSERT INTO items (itemID, itemName, itemPrice) VALUES (null, "BEER", 5)')
        # itemPrice = c.execute('SELECT itemPrice FROM items WHERE itemID = ?', ('1'))
        # for row in itemPrice:
        #
        #     print('itemPrice: ', row)
        # c.execute('DROP TABLE IF EXISTS saleItems')
        c.execute('CREATE TABLE IF NOT EXISTS saleItems(saleID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, itemName TEXT, saleItemQty INTEGER, saleItemPriceEach DECIMAL, saleItemTotal DECIMAL, saleDate TEXT, FOREIGN KEY (itemName) REFERENCES items (itemName));')
            # ,FOREIGN KEY (saleItemPriceEach) REFERENCES items (itemPrice) ON UPDATE CASCADE
        # c.execute('INSERT INTO saleItems(saleID, itemName, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate) VALUES (null, "BEER", 5, 5, 25, "2018-02-14" )')
        db.commit()

    except sqlite3.Error as err:
        print(err)

    # try:
    #     for item in items_dict:
    #         c.execute('INSERT OR REPLACE INTO items(indx, itemID, itemName, itemPrice) VALUES (null,?,?,?)', [items_dict['index'],items_dict['itemID'], items_dict['itemName'], items_dict['itemPrice']])
    #     db.commit()
        # data = textFilez.read_from_item_file_to_db()
        # print(data)
    #
    # except sqlite3.Error as err:
    #     print('{} = ERROR2'.format(err))
def add_sale_to_db(itemName, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate):
    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()
    c.execute('INSERT INTO saleItems(saleID, itemName, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate) VALUES (null,?,?,?,?,?);', (itemName, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate))
    # c.execute('DROP TABLE saleItems')
    db.commit()

def add_edit_item_to_db(itemName, itemPrice):
    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()
    rows_mod = c.execute('UPDATE items SET itemPrice = ? WHERE itemName = ?', (itemPrice, itemName))
    if rows_mod.rowcount == 0:
        c.execute('INSERT INTO items(itemID, itemName, itemPrice) VALUES (null,?,?);', (itemName,itemPrice))
    # c.execute('DROP TABLE saleItems')
    db.commit()

def show_items():
    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()
    c.execute('SELECT itemName, itemPrice FROM items')
    for row in c:
        print(row)

def show_menu():
    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()
    theList = []
    items_list = c.execute('SELECT itemID, itemName FROM items')
    for row in c:
        theList.append(row)
    return theList

def get_ids_list():
    ids = []
    db_filename  = "RMmgr_db.db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()
    c.execute('SELECT itemID from items')
    for i in c:
        ids.append(i)
    return ids
def main():
    setup_db()
    # add_item_to_db()

if __name__ == main():
    main()
