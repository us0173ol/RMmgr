import json


'''Lists for storage of db items'''

daily_sales_list = {}
weekly_sales_dict = {}
monthly_sales_dict = {}
items = {}


def add_edit_dict(itemName, itemPrice):
    items[itemName]=itemPrice

def show_items_dict():
    print(items)

def save_items_dict():
    json.dump(items, open("menu.txt", "w"))

def load_items_dict():
    items2 = json.load(open("menu.txt"))
    # print('items2: ', items2)
    items.update(items2)
    return items

def getItemPrice(itemName):
    itemPrice = items[itemName]
    # print('pricesss: ', itemPrice)
    return itemPrice

# def add_sale_to_dict(itemName, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate):
