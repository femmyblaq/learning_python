
from product import Product

class Order:
    def __init__(self):
        self.items = []
        self.quant = []

    def add_item(self, p : Product, q: int):
        self.items.append((p, q))
        print(f"Added {p} X {q} to product list.")
    def total(self):
        return sum(p.price * q for p, q in self.items )


order = Order()
laptop = Product("Laptop", 1500, 2)
bag = Product("Bag", 60, 1)
router = Product("Router", 90, 1)
order.add_item(laptop, 2)
order.add_item(bag, 3)
order.add_item(router, 4)

print(f"Total price order: ${order.total()}")