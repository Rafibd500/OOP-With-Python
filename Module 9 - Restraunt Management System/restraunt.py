from menu import Menu
class Restraunt:
    def __init__(self):
        self.employees = []
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} added successfully.')

    def view_employee(self):
        print("Name\tphone\temail\taddress\tdesignation\tsalary")
        for employee in self.employees:
            print(f'{employee.name}\t{employee.phone}\t{employee.email}\t{employee.address}\t{employee.designation}\t{employee.salary}')
