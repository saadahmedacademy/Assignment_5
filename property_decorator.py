
"""
18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. 
Use @property to get the price, @price.setter to update it, 
and @price.deleter to delete it.
"""


class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Test it
p = Product(100)
print(p.price)     # Getting the price

p.price = 150      # Setting new price
print(p.price)

del p.price        # Deleting the price
