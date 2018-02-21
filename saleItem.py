class SaleItem():


    Null_Index = None

    def __init__(self, saleID, itemID, saleItemQty, saleItemPriceEach, saleItemTotal, saleDate, index=Null_Index):

        self.index = index
        self.saleID = saleID
        self.itemID = itemID
        self.saleItemQty = saleItemQty
        self.saleItemPriceEach = saleItemPriceEach
        self.saleItemTotal = saleItemTotal
        self.saleDate = saleDate

    def set_index(self, index):
        self.index = index

    def __str__(self):

        if self.index is None:
            index_str = '(none)'
        else:
            index_str = self.index


        saleItemStr = 'index: {}, saleID: {} \t itemID: {} \t saleItemQty {} \t saleItemPriceEach {} \t saleItemTotal {} \t saleDate {}'
        return saleItemStr.format(self.index, self.saleID, self.itemID, self.saleItemQty, self.saleItemPriceEach, self.saleItemTotal, self.saleDate)
