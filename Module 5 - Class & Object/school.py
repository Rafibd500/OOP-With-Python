class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    def __repr__(self):
        return f'name:{self.name}, class: {self.current_class}, id: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f'Teacher Name: {self.name}, subject: {self.subject}, id: {self.id}'
    

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_teacher(self, name, subject):
        id = len(self.teachers)+101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    

# rahim = Student('Rahim', 11, 101)
# pias = Teacher('Mahmud Pias', 'Algorithm', 201)
# print(rahim)
# print(pias)
my_school = School('My School')
my_school.add_teacher('Kuddus ali', 'DS')
my_school.add_teacher('udhvut ali', 'Stat')
my_school.add_teacher('kudvut ali', 'Algo')
print((my_school.teachers[0].id))
