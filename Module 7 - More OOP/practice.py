
class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.product_name}, {self.price}, {self.quantity}'

class Shop:
    def __init__(self, name):
        self.name = name
        self.list = []
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.list.append(product)

    def buy_product(self, name, quantity):
        found = False
        for product in self.list:
            if(product.product_name == name):
                if(quantity<=product.quantity):
                    print(f'thanks for your order. total: {quantity*product.price}.')
                    product.quantity -= quantity
                else:
                    print(f'Product available. But Only {product.quantity} are left.')
                found = True
                break
        if(found == False): print("Product not available")

def show_product():
    print('========Available product======')
    for product in shwapno.list:
        print(product)

shwapno = Shop('shwapno')
shwapno.add_product('pen', 200, 500)
shwapno.add_product('paper', 100, 700)
shwapno.add_product('pencil', 50, 1000)
show_product()
shwapno.buy_product('pencil', 50)
shwapno.buy_product('pen', 1)
shwapno.buy_product('paper', 1000)
show_product()


'''
# What is Inheritance? Explain with examples
ans: inheritance is a key pillar of oop. It is a method where we make a common class with the common instance of several instance. Other way we can say that we make a Parent class where we store the common instance/attribute, method of Child classes. Ex: Vehical(parent class) -> Car/Bus/Truck(child class).

refine ans with chatgpt: Inheritance is a key pillar of Object-Oriented Programming (OOP).
It is a mechanism that allows one class (called the child class or subclass) to inherit attributes and methods from another class (called the parent class or superclass).
This helps to reuse code, reduce redundancy, and maintain a clear class hierarchy.
Example:
Vehicle → parent class (contains common attributes like brand, color, speed)
Car, Bus, Truck → child classes (inherit from Vehicle and may add their own features).
'''
# ===============================
'''
# What are Encapsulation and Access Modifiers? Explain with examples
ans: 🧩 Encapsulation

Encapsulation is one of the main principles of Object-Oriented Programming (OOP).
It means wrapping data (variables) and methods (functions) that work on that data into a single unit — a class.
It also helps to hide the internal details of an object from the outside world, allowing data protection and controlled access.

In short:

Encapsulation = Data hiding + Controlled access through methods

Example (Python):

class Student:
    def __init__(self, name, age):
        self.name = name        # public variable
        self.__age = age        # private variable (hidden)

    def get_age(self):
        return self.__age       # public getter

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age


Here, __age is hidden from outside direct access.
You can only access it using get_age() or modify it with set_age() — that’s encapsulation.

🔐 Access Modifiers

Access modifiers define how much access other parts of the program have to the class members (attributes and methods).
In Python, we use naming conventions to indicate access level:

Modifier	Syntax	Meaning
Public	variable	Accessible from anywhere
Protected	_variable	Should be accessed only inside the class and its subclasses
Private	__variable	Hidden from outside access (name mangling applies)

Example:

class Employee:
    def __init__(self):
        self.name = "Rafi"        # public
        self._salary = 50000      # protected
        self.__bonus = 10000      # private


emp.name → accessible ✅

emp._salary → can be accessed, but not recommended ❌

emp.__bonus → cannot be accessed directly ❌

🧠 In summary:

Encapsulation protects data by bundling it with related methods.

Access Modifiers control who can access or modify that data.
'''