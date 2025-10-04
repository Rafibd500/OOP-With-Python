# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.


class User:
    def __init__(self, name, id, age, salary):
        self._name = name
        self.id = id
        self.__age = age
        self.__salary = salary
    #getter
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, x):
        self.__age += x
user1 = User("user1", 100, 24, 20000)
# user1.__salary
print(user1.age)
user1.age = 100
print(user1.age)
