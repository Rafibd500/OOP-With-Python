
class Phone:
    def __init__(self, name, company, color, ram, rom, display):
        self.name = name
        self.company = company
        self.color = color
        self.ram = ram
        self.rom = rom
        self.display = display
    def device_type(self):
        print("this is a electronics device")
    def calling():
        print("Phone can calling to anyone")
    
class Headphone:
    def __init__(self, name, company, color, sound_quality, anc):
        self.name = name
        self.company = company
        self.color = color
        self.sound_quality = sound_quality
        self.anc = anc
    def device_type(self):
        print("this is a electronics device")
    def listening():
        print("we can listen song with headphobe")
class Keyboard:
    def __init__(self, name, company, color, keycaps, switch_type):
        self.name = name
        self.company = company
        self.color = color
        self.keycaps = keycaps
        self.switch_type = switch_type
    def device_type(self):
        print("this is a electronics device")
    def typing():
        print("we can type with keyboard")


"""
ekhane sobgulo class ei kihu attrubute and method same. jemon:
name, company, color
so amra eguloke alada ekta class e rakhte pari. like:
"""
class Device:
    def __init__(self, name, company, color):
        self.name = name
        self.company = company
        self.color = color
    def device_type(self):
        print("this is a electronics device")


"""
And that call inheritance

ekhane :
Device - parent class, base class, common attribute & functionality class
Phone, Headphone, Keybaord - child class, derived class, uncommon attribute & functionality class


"""