from dicts import *
from saleItem import *
import textFiles
import items
import theDB

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

    message = 'New sale'
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)

    message ='Items to choose from, itemID is the first number in the row. '
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)


    #
    # print(theList)
    # for i in theList:
    #     for j in i:
    #         print('j: ', j)
    #     print('i:', i)


    while True:
        try:
            theList = theDB.show_menu()
            print(theList)
            itemID = input('Please enter the ID number for the item being sold. ')
            itemID = int(itemID)
            for i in theList:
                for j in i:
                    if itemID == j:
                        print('Success')
                    else:
                        break
                break
            break
        except ValueError:
            message('Invalid entry1, no decimal or negative numbers')
    while True:
        try:
            saleItemQty = int(input('How many sold? Enter whole numbers only'))
            if saleItemQty < 0:
                print('Please enter a positive whole number')
            else:
                break
        except ValueError:
            print('Invalid entry2, no decimal or negative numbers')
    while True:
        try:
            saleItemPriceEach = getItemPrice(itemId)
        except ValueError:
            print('Could not find item price in list')
    while True:
        try:
            saleItemTotal = saleItemQty * saleItemPriceEach
        except ValueError:
            print('Error')
    print('Name: ', itemID, 'Qty: ', saleItemQty, 'Price: ', saleItemPriceEach, 'Total: ', saleItemTotal)
def getItemPrice(itemID):
    itemPrice = extract_price(itemID)
    return itemPrice

def add_edit_items():

    message = ('Add to/Edit Items Menu')
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)
    # print(theDB.show_items())

    itemName = str(input('Enter the name of the item you would like to add/edit. '))
    itemPrice = float(input("Enter the price of the item. "))
    items_list = theDB.add_edit_item_to_db(itemName.upper(), itemPrice)
    for row in items_list:
        print('ROW: ', row)





# def daily_sales():
#
# def weedly_sales():
#
# def monthly_sales():
#
# def sales_by_item():
























def message(msg):
    print(msg)
