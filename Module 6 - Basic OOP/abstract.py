from abc import ABC, abstractmethod

class Animal(ABC):
    # @abstractmethod
    def eat(self):
        print("I am eating")
    def run(self):
        print("I am running")

class Monkey(Animal):
    def __init__(self, name):
        self.name = name
        self.category = "Moneky"
        super().__init__()
    # def eat(self):
    #     print("I am called from monkey class")

monka = Monkey('Monka')
monka.eat()
monka.run()