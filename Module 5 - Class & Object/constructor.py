class Phone:
    manufactured = 'China'

    def __init__(self, owner, name, ram, rom):
        self.owner = owner
        self.name = name
        self.ram = ram
        self.rom = rom

my_phone = Phone('Rafi', 'samsung', '8gb', '256gb')
his_phone = Phone('He', 'iPhone', '6gb', '128gb')
print(my_phone.owner, my_phone.name, my_phone.ram, my_phone.rom)
print(his_phone.owner, his_phone.name, his_phone.ram, his_phone.rom)
print(my_phone.owner, my_phone.name, my_phone.ram, my_phone.rom)

# Homework on constructor
print('')
class Pen:
    reason = 'Writing'
    def __init__(self, company, length, color):
        self.company = company
        self.length = length
        self.color = color
matador_pen = Pen('Matador', 20, 'red')
good_luck_pen = Pen('Good luck', 18, 'green')
econo_pen = Pen('Econo', 15, 'blue')
print(matador_pen.company, f'{matador_pen.length} cm', matador_pen.color)
print(good_luck_pen.company, f'{good_luck_pen.length} cm', good_luck_pen.color)
print(econo_pen.company, f'{econo_pen.length} cm', econo_pen.color)