from lists import daily_sales_list, items_list, monthly_sales_list, weekly_sales_list
import sqlite3

class textFilez():


    def write_to_item_file():
        filename = 'items.txt'
        with open(filename, 'w') as f:
            for item in items_list:
                f.write("%s \n" % item)

    def read_from_item_file_to_db():
        filename = 'items.txt'
        with open(filename, 'r') as f:
            return f.readlines()
