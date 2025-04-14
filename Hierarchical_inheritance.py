class Person:
    def show_name(self):
        print(" I am a show name method")

class Teacher(Person):
    def teach(self):
        print("i am a teach method")

class Student(Person):
    def study(self):
        print('i am study method')

teacher=Teacher()
teacher.teach()
teacher.show_name()

student=Student()
student.study()
student.show_name()
