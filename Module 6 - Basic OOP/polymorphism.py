# Poly = many, Morph = forms
# Polymorphism = one thing behaving in many ways

class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Mewo mewo")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("gheu gheu")
class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("baa baa")
catty = Cat('catty')
doggy = Dog("Doggy")
goatty = Goat("goatty")

catty.sound()
doggy.sound()
goatty.sound()