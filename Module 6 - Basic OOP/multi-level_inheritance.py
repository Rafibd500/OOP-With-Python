class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def move(self):
        print("this function is moving.")

class Bus(Vehicle):
    def __init__(self, name, color, price, seat, condition):
        self.seat = seat
        self.condition = condition
        super().__init__(name, color, price)
    def bus(self):
        print("bus is moving fast")

class AcBus(Bus):
    def __init__(self, name, color, price, seat, condition, temp):
        self.temp = temp
        super().__init__(name, color, price, seat, condition)
    def ac(self):
        print("weather feeling so cold")
class Greenline(AcBus):
    def __init__(self, name, color, price, seat, condition, temp, stopage):
        self.stopage = stopage
        super().__init__(name, color, price, seat, condition, temp)

    def __repr__(self):
        return f'{self.color} {self.stopage}'


greenLine = Greenline('Green line master', 'lal', 800, 44, 'new', "25 deg", "Mirpur")
print(greenLine)
greenLine.move()