import random
from school import School
class Person:
    def __init__(self, name):
        self.name = name
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def teach(self):
        pass
    def evalute_exam(self):
        return random.randint(1,100)
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classroom = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
        self.__student_id = None

    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            sum += School.grade_to_value()
        return sum/len(self.subject_grade)

    @property
    def id(self):
        return self.__student_id
    @id.setter
    def id(self, new_id):
        self.__student_id = new_id