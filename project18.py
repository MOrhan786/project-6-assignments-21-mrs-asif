#18. Property Decorators: @property, @setter, and @deleter
#Assignment:
#Create a class Product with a private attribute _price. Use @property to get the price,
# @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price
    
    # Getter
    @property
    def price(self):
        return self._price
    
    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value
    
    # Deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Creating an instance of the Product class
product = Product(100)

# Accessing the price using the getter
print("Price:", product.price)

# Updating the price using the setter
product.price = 150
print("Updated Price:", product.price)

# Trying to set a negative price (will trigger validation)
product.price = -50

# Deleting the price using the deleter
del product.price

