class StudentDatabase:
    student_list = []
    def __init__(self):
        pass
    def add_student(self, name, department, is_enrolled):
        student_id = len(self.student_list)+1001
        student = Student(student_id, name, department, is_enrolled)
        self.student_list.append(student)
    
class Student(StudentDatabase):
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.name = name
        self._department = department
        self.__is_enrolled = is_enrolled
    
    @classmethod
    def view_student_info(self):
        for student in self.student_list:
            print(f'ID: {student.__student_id}, Name: {student.name}, Department: {student._department}, Enrolled: {student.__is_enrolled}')
    @classmethod
    def find_student(self, id):
        for student in self.student_list:
            if(student.__student_id == id):
                return student
        return False
    def enroll_student(self, student):
        if(student.__is_enrolled == True):
            print("!!! Student Already Enrolled")
        else:
            student.__is_enrolled = True
            print(f'Student ID: {student.__student_id} enrolled successfully')
    def drop_student(self, student):
        if(student.__is_enrolled == False):
            print("!!! Student haven't enroll course.")
        else:
            student.__is_enrolled = False
            print(f'Student ID: {student.__student_id} Dropped successfully')
    def __repr__(self):
        return (f'{self.__student_id}, {self.name}, {self._department}, {self.__is_enrolled}')

phitron = StudentDatabase()
phitron.add_student('Rahim', 'SWE', False)
phitron.add_student('Kahim', 'CSE', True)
phitron.add_student('Rakib', 'CIS', False)
phitron.add_student('Sakib', 'ITM', True)
phitron.add_student('Tanvi', 'ICE', True)
phitron.add_student('Karim', 'MCT', True)

while True:
    print('========= Phitron ========')
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')
    choice = int(input('Enter Your choice: '))
    if choice == 1:
        print("---------- Student List ----------")
        Student.view_student_info()
    elif choice == 2:
        id = int(input('Enter student ID: '))
        student = Student.find_student(id)
        if(student): student.enroll_student(student)
        else: print(f"Student Not exist with ID: {id}")
    elif choice == 3: 
        id = int(input('Enter student ID: '))
        student = Student.find_student(id)
        if(student): student.drop_student(student)
        else: print(f"Student Not exist with ID: {id}")
    elif choice == 4: break
    else : print("Invalid Choice. Please try with valid one")