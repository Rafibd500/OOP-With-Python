# All classes will write here
from abc import ABC
from order import Order
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    def view_menu(self, restraunt):
        restraunt.menu.view_items()
    def add_to_cart(self, restraunt, item_name, quantity):
        item = restraunt.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Not enough quantity in stock.")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added to the cart")
        else:
            print('Item Not found')

    def view_cart(self):
        print("*****View Cart*****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

    def total_price(self):
        print(f"Total Price: {self.cart.total_price}")
    
    def pay_bill(self):
        print(f"Total {self.cart.total_price} tk paid successfully")
        self.cart.clear()



class Employee(User):
    def __init__(self, name, phone, email, address, designation, salary):
        super().__init__(name, phone, email, address)
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self,restraunt, employee):
        restraunt.add_employee(employee)

    def view_employee(self, restraunt):
        restraunt.view_employee()
    
    def add_item(self, restraunt, item):
        restraunt.menu.add_menu_item(item)
    def view_menu(self, restraunt):
        restraunt.view_menu()
    def remove_item(self, restraunt, item):
        restraunt.menu.remove_item(item)





# res = Restraunt()
# admin = Admin('admin', '1202', 'ewkj', 'kjkj')
# foodMenu = Menu()
# item = FoodItem('Burger', 100, 5)
# item1 = FoodItem('Pizza', 200, 10)
# item2 = FoodItem('z', 200, 10)
# admin.add_item(res, item)
# admin.add_item(res, item1)
# admin.add_item(res, item2)
# # foodMenu.add_menu_item(item)
# # foodMenu.view_items()     


# customer1 = Customer('Rahim',"029309309", "rahim@gg.co", 'dhaka, bd')
# customer1.view_menu(res)

# item_name =input("Enter a item name:")
# quantity = int(input("Enter the quantity: "))
# customer1.add_to_cart(res, item_name, quantity)
# customer1.view_cart()
# customer1.total_price()