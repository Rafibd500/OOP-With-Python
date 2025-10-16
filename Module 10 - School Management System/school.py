class School:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        teachers = {}    # {"bangla" : teacher_object}
        classrooms = {}    # {"eight" : classroom_object}
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, teacher, subject):
        self.teachers[subject] = teacher
    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)
    

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks >=70:
            return 'A'
        elif marks >= 60:
            return 'A-'
        elif marks >= 50:
            return 'B'
        elif marks >=40:
            return 'C'
        elif marks >= 33:
            return 'D'
        elif marks <33 and marks>=0:
            return 'F'
        else: 
            return "Invalid"
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    def __repr__(self):
        # All Classrooms
        print("*******All classroom*******")
        for key in self.classrooms.keys():
            print(key)
        # All Students
        print("*******All Students*******")
        result = ''
        for classroom in self.classrooms.values():
            result += f"{classroom.name}--->"
            for student in classroom.students:
                print(student.name)
        print(result)
        # All Subjects
        print("*******All Students*******")
        result1 = ''
        for classroom in self.classrooms.values():
            result1 += f"{classroom.name}--->"
            for subject in classroom:
                result1 += f"{subject.name}"
        # All Teachers - Homework
        print("*******All Teachers*******")
        for teacher in self.teachers.values():
            print(teacher)
        # All Student Results
        print("*******Student Result*******")
        for key, val in self.classrooms.items():
            for student in val.students:
                for k, i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[i])
                print(student.calculate_final_grade())
        return ''