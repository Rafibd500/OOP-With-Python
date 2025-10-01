class Calculator:
    name = "Casio 991ex Plus"
    def add(self, *list):
        s = 0
        for n in list:
            s+=n
        return s
    def substruction(self, a, b):
        return a-b
    def multiply(self, *list):
        multi = 1
        for n in list:
            multi *= n
        return multi
    def devision(self, a, b):
        return a//b
    
calculator_1 = Calculator()
print(calculator_1.name)
print(calculator_1.add(10, 20, 40))
print(calculator_1.substruction(50, 20))
print(calculator_1.multiply(10, 20, 40))
print(calculator_1.devision(10,5))