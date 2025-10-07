# All classes will write here
from abc import ABC
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None
    def view_menu(self, restraunt):
        restraunt.menu.view_items()
    def add_to_cart(self, restraunt, item):
        item = restraunt.menu.find_item(item)
        if item:
            pass
        else:
            print('Item Not found')

    def view_cart(self):
        pass
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

    def remove_item(self, restraunt, item):
        restraunt.menu.remove_item(item)

class Restraunt:
    def __init__(self):
        self.employees = []
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} added successfully.')

    def view_employee(self):
        for employee in self.employees:
            print(f'{employee.name}, {employee.phone}, {employee.email}, {employee.address}, {employee.designation}, {employee.salary}')



class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)
        print(f'{item.name} added to menu.')

    def find_item(self, item_name):
        for item in self.items:
            if(item.name.lowe() == item_name.lower()): return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item: self.items.remove(item); print('Item deleted.')
        else : print('Item Not found.')
    
    def view_items(self):
        print("********* Menu **********")
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item = FoodItem('Burger', 100, 5)
foodMenu = Menu()
# foodMenu.add_menu_item(item)
res = Restraunt()
admin = Admin('admin', '1202', 'ewkj', 'kjkj')
admin.add_item(res, item)
foodMenu.view_items()     
admin.add_item(res, item)
