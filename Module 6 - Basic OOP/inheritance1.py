class Device:
    def __init__(self, name, company, color):
        self.name = name
        self.company = company
        self.color = color
    def device_type(self):
        print("this is a electronics device")


class Phone(Device):
    def __init__(self, name, company, color, ram, rom, display):
        self.ram = ram
        self.rom = rom
        self.display = display
        super().__init__(name, company, color)
    def calling(self):
        print("Phone can calling to anyone")
    
class Headphone(Device):
    def __init__(self, sound_quality, anc):
        self.sound_quality = sound_quality
        self.anc = anc
    def listening():
        print("we can listen song with headphobe")
class Keyboard:
    def __init__(self, keycaps, switch_type):
        self.keycaps = keycaps
        self.switch_type = switch_type
    def typing():
        print("we can type with keyboard")


samsung = Phone("s25 ultra", "samsung", "lal", "16gb", "256gb", "10 inch")
print(samsung.name)
samsung.device_type()
havit = Headphone('low', 'Yes')
havit.device_type()