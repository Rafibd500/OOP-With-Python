class Student:
    def __init__(self, id, name, age, cgpa):
        self.id = id
        self.name = name 
        self.age = age
        self.cgpa = cgpa
    def calling(self):
        print("I am calling from student block")

class Swe_dept(Student):
    def __init__(self, id, name, age, cgpa, lab):
        super().__init__(id, name, age, cgpa)
        self.lab = lab
    # override
    def calling(self):
        print('i am calling from swe_dept block')

    # overloading
    # for add
    def __add__(self, other):
        return self.age + other.age
    
    # for multiplication
    def __mul__(self, other):
        return self.age * other.age

    # for greater than
    def __mul__(self, other):
        return self.age > other.age
    
    # for len
    def __len__(self):
        return self.age
    
habu = Swe_dept('101', 'Habu', 45, 4.99, 'I am lab')
pasha = Swe_dept('102', 'Pasha', 55, 5.99, 'I am lab')
habu.calling()


# overloading
print(5+10)
print(5*10)
print([10,20]+[30, 40, 50])

print(habu+pasha)
print(habu*pasha)
print(len(habu))

# overloading
# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types