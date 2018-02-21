class Item:

    '''Each item that is on the menu(for now, can add more later)'''
    '''Will also be used to add items to the menu and change prices'''

    Null_Index = None

    def __init__(self, itemName, itemPrice, index=Null_Index,  itemID=Null_Index):

        self.index = index
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice

    def set_index(self, index):
        self.index = index

    def __str__(self):

        if self.index is None:
            index_str = '(none)'
        else:
            index_str = self.index



        itemStr = 'Index: {}   ItemID: {}   ItemName: {}   ItemPrice: ${:.2f}'
        return itemStr.format(self.index, self.itemID, self.itemName.title(), self.itemPrice)
