from dicts import *
from saleItem import *
import textFiles
import items
import theDB
import datetime
from datetime import date, datetime

def show_main_menu():

    validChoice = False
    main_choice = ''

    message = '''Main Menu'''
    line = "_" * len(message) *4
    print('\n', line, '\n', message, '\n', line)
    print( '''----ENTER A NUMBER----
    1. Start RM Program
    2. Daily Sales
    3. Weekly Sales
    4. Monthly Sales
    5. Sales by item
    q. Quit
    ''')


    while not validChoice:
        main_choice = input('Please make a selection \n')
        if (main_choice != '1' and main_choice != '2' and main_choice !='3'
                and main_choice != '4' and main_choice != '5' and main_choice != 'q'):
                print('Error, please choose 1-5 or q')
        else:
            validChoice = True
    return main_choice

def start_RM_program():
    validChoice = False
    RMchoice = ''

    message = '''RM Program'''
    line = "_" * len(message) *4
    print('\n', line, '\n', message, '\n', line)
    print ('''----Enter a number----
    1. New Sale
    2. Edit a Sale
    3. Delete a Sale
    4. Add/Edit Items and Prices
    5. Back to Main Menu
    ''')


    while not validChoice:
        RMchoice = input('Please make a selection \n')
        if (RMchoice != '1' and RMchoice != '2' and RMchoice !='3' and RMchoice !='4'
                and RMchoice != '5'):
                print('Error, please choose 1-5')
        else:
            validChoice = True
    return RMchoice



def add_a_sale():
    items = load_items_dict()
    # print('ITEMZ: ', items)
    message = 'New sale'
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)

    message ='Items to choose from. '
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)

    theDB.show_items()
    itemName = input('Please enter the name of the item being sold...')
    while itemName in items:
        saleItemQty = int(input('How many sold? Enter whole numbers only...'))
        while saleItemQty > 0:
            saleItemPriceEach = getItemPrice(itemName)
            saleItemTotal = saleItemQty * saleItemPriceEach
            saleDate = date.today()
            break
        break


    print('Name: ', itemName, 'Qty: ', saleItemQty, 'Price: ', saleItemPriceEach, 'Total: ', saleItemTotal, 'Date: ', saleDate )

    theDB.add_sale_to_db(itemName, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate)



def add_edit_items():
    load_items_dict()
    message = ('Add to/Edit Items Menu')
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)
    # print(theDB.show_items())

    itemName = str(input('Enter the name of the item you would like to add/edit. '))
    itemPrice = float(input("Enter the price of the item. "))
    add_edit_dict(itemName, itemPrice)
    items_list = theDB.add_edit_item_to_db(itemName.upper(), itemPrice)
    show_items_dict()
    save_items_dict()
    # for row in items_list:
    #     print('ROW: ', row)





# def daily_sales():
#
# def weedly_sales():
#
# def monthly_sales():
#
# def sales_by_item():
























def message(msg):
    print(msg)
