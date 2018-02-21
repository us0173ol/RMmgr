import sqlite3
from textFiles import textFilez
import csv

def setup_db():


    db_filename  = "RMmgr_db"
    db = sqlite3.connect(db_filename)
    c = db.cursor()

    try:
        c.execute('PRAGMA foreign_keys=ON')
        c.execute('CREATE TABLE IF NOT EXISTS items(indx INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, itemID INTEGER NOT NULL AUTOINCREMENT, FOREIGN KEY (itemID) REFERENCES saleItems (itemID), itemName TEXT, itemPrice DECIMAL, FOREIGN KEY (itemPrice) REFERENCES saleItems (saleItemPriceEach));')
        c.execute('CREATE TABLE IF NOT EXISTS saleItems(indx INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, saleID INTEGER NOT NULL AUTOINCREMENT, itemID INTEGER, FOREIGN KEY (itemID) REFERENCES items (itemID), saleItemQty INTEGER, saleItemPriceEach DECIMAL, FOREIGN KEY (saleItemPriceEach) REFERENCES items (itemPrice), saleItemTotal DECIMAL, saleDate VARCHAR(10));')
        db.commit()

    except sqlite3.Error as err:
        print('{} = ERROR'.format(err))

    try:
        data = textFilez.read_from_item_file_to_db()
        print(data)

    except sqlite3.Error as err:
        print('{} = ERROR2'.format(err))

def main():
    setup_db()

if __name__ == main():
    main()
