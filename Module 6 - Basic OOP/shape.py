from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, name, width, length):
        self.width = width
        self.length = length
        super().__init__(name)
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return self.radius*self.radius*pi
    
rec = Rectangle("my Rectangle", 20, 30)
print(rec.area())
cir = Circle("my Circle", 5)
print(cir.area())
