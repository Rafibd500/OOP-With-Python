# simply: method holo class er vitor ekta function
class Student:
    name = 'sakib'
    roll = 200

    def call(self):
        print("I'm calling the function")

    def call2(self, *list):
        print(list)
student1 = Student()
student1.call2(10,20,30,40,50)