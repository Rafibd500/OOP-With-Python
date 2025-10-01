class Shop:
    cart = []
    def __init__(self, customer_name):
        self.customer_name = customer_name
    def add_to_cart(self, product_name):
        self.cart.append(product_name)

rafi = Shop('rafi')
rafiqul = Shop('rafiqul')
rafiqul.add_to_cart('1')
rafi.add_to_cart("pen")
rafiqul.add_to_cart('2')
rafi.add_to_cart("phone")
rafi.add_to_cart("ID Card")
print(rafiqul.cart)
print(rafi.cart)