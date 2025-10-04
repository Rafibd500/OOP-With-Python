class Book:
    def __init__(self, name):
        self.name = name
    def read(self):
        raise NotImplementedError 
class Physics(Book):
    def __init__(self, name, lab):
        self.lab = lab
        super().__init__(name)
    def read(self):
        print('Tapan Physics book')
    def __repr__(self):
        return f'{self.name} {self.lab}'
    
tapan = Physics('Tapan Books', 'Lab class')
print(tapan)
print(issubclass(Physics, Book))
print(isinstance(tapan, Physics))
print(isinstance(tapan, Book))
tapan.read()