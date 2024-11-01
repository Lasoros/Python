class Product:
    def __init__(self, price):
        self.price = price


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Value cannot be less than zero. . .")
        self.__price = value


    #price = property(get_price, set_price) #note not calling get_price() but simply passing a referance

# Above code is 'UnPythonic", or not using Python to its fullest

# A Property is an object that sits in front of a attribute and allows to get or set that value




product = Product(10)

#product,price = -1

print(product.price)