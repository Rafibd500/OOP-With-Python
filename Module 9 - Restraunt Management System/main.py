from food_item import FoodItem
from menu import Menu
from order import Order
from restraunt import Restraunt
from users import Customer, Admin, Employee

restraunt = Restraunt()
# create customer
def customer_menu():
    name = input("Enter your name: ")
    phone = input("Enter yuur phone number: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")

    customer = Customer(name, phone, email, address)
    while 1:
        print(f"Welcome {customer.name}.")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            restraunt.menu.view_items()
        elif choice == 2:
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(restraunt, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice  == 5:
            break
        else: print("Invalid choice")

def admin_menu():
    name = input("Enter your name: ")
    phone = input("Enter yuur phone number: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")

    admin = Admin(name, phone, email, address)
    
    while 1:
        print(f"Welcome {admin.name}.")
        print("1. Add new Item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_item(restraunt, item)
            print()
        elif choice == 2:
            name = input("Enter Employee name: ")
            phone = input("Enter Employee phone number: ")
            email = input("Enter Employee email: ")
            address = input("Enter Employee address: ")
            designation = input("Enter Employee designation: ")
            salary = int(input("Enter Employee salary: "))
            employee = Employee(name, phone, email, address, designation, salary)
            admin.add_employee(restraunt, employee)
            print()
        elif choice == 3:
            admin.view_employee()
            print()
        elif choice == 4:
            restraunt.menu.view_items()
            admin.view_menu(restraunt)
            print()
        elif choice  == 5:
            name = input("Enter menu item name: ")
            admin.remove_item(name)
            print()
        elif choice  == 6:
            break
        else: print("Invalid choice", end = '\n')


admin_menu()