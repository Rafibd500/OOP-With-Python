# All classes will write here
from abc import ABC
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class Employee(User):
    def __init__(self, name, phone, email, address, designation, salary):
        super().__init__(name, phone, email, address)
        self.designation = designation
        self.salary = salary
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []
    def add_employee(self, name, phone, email, address, designation, salary):
        employee = Employee(name, phone, email, address, designation, salary)
        self.employees.append(employee)
        print(f'{name} added successfully.')
    def view_employee(self):
        for employee in self.employees:
            print(f'{employee.name}, {employee.phone}, {employee.email}, {employee.address}, {employee.designation}, {employee.salary}')
ad = Admin('Admin', '101929', 'admin@admin.com', 'Dhaka')            
ad.add_employee('Rahim', '9844938', 'rahim@g.com', 'Dhaka', 'Software Engineer L2', '200000')       
ad.view_employee()     
