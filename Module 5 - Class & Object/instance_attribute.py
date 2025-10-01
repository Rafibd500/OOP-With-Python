class Shop:
    name = "ABC IT Shop"
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, name):
        self.cart.append(name)
rafi = Shop('rafi')
rafiqul = Shop('rafiqul')
rafiqul.add_to_cart('1')
rafi.add_to_cart("pen")
rafiqul.add_to_cart('2')
rafi.add_to_cart("phone")
rafi.add_to_cart("ID Card")
print(rafiqul.name, end = ": ")
print(rafiqul.cart)
print(rafi.name, end = ": ")
print(rafi.cart)