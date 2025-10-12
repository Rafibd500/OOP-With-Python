class School:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        teachers = {}
        classrooms = {}
    
    def add_classroom(self, classroom){
        pass
    }
    def add_teacher(self, teacher){
        pass
    }
    def student_admission(self, student){
        pass
    }

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