class Shop:
    # cart = []       # common attribute
    def __init__(self, name):
        self.cart = []      # instance attribute
        self.name = name    
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.cart.append(product)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return (f"{self.name}, {self.price}, {self.quantity}")

shop1 = Shop('Dushopno')
shop1.add_product('alu', 20, 50)
shop1.add_product('chal', 60, 90)
for prod in shop1.cart:
    print(prod)
print('\n')
shop2 = Shop('tinshopno')
shop2.add_product('potol', 40, 100)
shop2.add_product('dal', 120, 300)
for prod in shop2.cart:
    print(prod)


""" 
Brac Bank [class atribute]
 - Dhaka Branch
 - Rajshahi Branch [instance attribute]
"""
