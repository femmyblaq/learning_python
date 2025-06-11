class Product:
    def __init__(self, pName, price, stock):
        self.pName = pName
        # self.quantity = quantity
        self.price = price
        self.stock = stock

    def is_in_stock(self, quantity):
        return self.stock >= quantity
    
    
# p1 = Product("Air fryer", 2, 3)
# print(p1.is_in_stock(2))

