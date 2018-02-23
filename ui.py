import dicts
import saleItem
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
                and RMchoice != 'b'):
                print('Error, please choose 1-4 or b')
        else:
            validChoice = True
    return RMchoice


'''MOVE TO DATASTORE
def populateItems():
    menuItem1 = Items('1', 'Beer', '4')
    menuItem2 = Items('2', 'Wine', '7')
    menuItem3 = Items('3', 'Liqour', '8')
    menuItem4 = Items('4', 'Food', '10')
    '''




def add_a_sale():

    message('New sale')
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)

    message('Items to choose from, itemID is the first number in the row. ')
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)

    for item in items_dict:
        message(item)


    while True:
        try:
            itemId = int(input('Please enter the itemID number for the item being sold. '))
            if itemId not in items_dict:
                message('Please enter a valid choice. ')
            else:
                break
        except ValueError:
            message('Invalid entry1, no decimal or negative numbers')
    while True:
        try:
            saleItemQty = int(input('How many sold? Enter whole numbers only'))
            if saleItemQty < 0:
                message('Please enter a positive whole number')
            else:
                break
        except ValueError:
            message('Invalid entry2, no decimal or negative numbers')
    while True:
        try:
            saleItemPriceEach = getItemPrice(itemId)
        except ValueError:
            message('Could not find item price in list')
    while True:
        try:
            saleItemTotal = saleItemQty * saleItemPriceEach
        except ValueError:
            message('Error')



def getItemPrice(ItemID):
    for item in items_dict:
        if item == item:
            saleItemPriceEach = items.Item.itemPrice
    return saleItemPriceEach

def add_items():

    message = ('Add Items to Menu')
    line = "_" * len(message)
    print('\n', line, '\n', message, '\n', line)

    itemName = str(input('Enter the name of the item you would like to add. '))
    itemPrice = float(input("Enter the price of the item. "))
    key = len(dicts.items_dict) + 1
    dicts.items_dict.setdefault(key, [])
    print("key: ", key)
    # return itemName, itemPrice

    itemToAdd = items.Item( itemName, itemPrice)
    print (itemToAdd)

    itemname = itemToAdd.itemName
    itemprice = itemToAdd.itemPrice
    dicts.items_dict[key].append(itemName)
    dicts.items_dict[key].append(itemPrice)
    # dicts.items_dict.update({key,itemname,itemprice})

    print("DictItems: ", dicts.items_dict)

    textFiles.textFilez.write_to_item_file()
    textFiles.textFilez.read_from_item_file_to_db()

    for item in dicts.items_dict:
        print ("item in dict: ", item)




# def daily_sales():
#
# def weedly_sales():
#
# def monthly_sales():
#
# def sales_by_item():
























def message(message):
    print(message)
