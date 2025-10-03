# simple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Animals make sound")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def __repr__(self):
        return f'{self.name} + {self.breed}'
    def make_sound(self):
        print("Dog barks")
    
dog = Dog('Tommy', 'don\'t know')
# print(dog)
# dog.make_sound()


# Task 2 - Multi-level inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, student_id):
        self.student_id = student_id
        super().__init__(name, age)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, degree):
        self.degree = degree
        super().__init__(name, age, student_id)
    def __repr__(self):
        return f'name: {self.name}, age: {self.age}, student id: {self.student_id}, degree: {self.degree}'
grad_student = GraduateStudent('Kuddus', 25, '201', 'B.Sc in SWE')
# print(grad_student)

# Task 3 - Multiple Inheritance
class Teacher:
    def teach(self):
        print("teaches a subject")
class Artist:
    def draw(self):
        print("create an artwork")
class CreativeTeacher(Teacher, Artist):
    # def __init__(self):
    #     Teacher.__init__(self)
    #     Artist.__init__(self)
    def show_skill(self):
        print("can teach and draw")

# ct = CreativeTeacher()
# ct.teach()
# ct.draw()
# ct.show_skill()

# Task 4 - Hybrid Inheritance
class Device:
    def __init__(self, brand):
        self.brand = brand
class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
class Camera(Device):
    def __init__(self, brand, resulation):
        super().__init__(brand)
        self.resulation = resulation
class SmartPhone(Phone, Camera):
    def __init__(self, brand, model, resulation, ram, rom):
        self.ram = ram
        self.rom = rom
        Phone.__init__(self, brand, model)
        Camera.__init__(self, brand, resulation)        
    def __repr__(self):
        return f'{self.brand}, {self.model}, {self.resulation}, {self.ram}, {self.rom}'
iphone = SmartPhone("Apple", 'iPhone 18 pro max', '200px', '16gb', '256gb')
print(iphone)