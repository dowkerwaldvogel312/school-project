class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("张三", 18)
student2 = Student("李四", 17)

for student in [student1, student2]:
    print(f"{student.name} is {student.age} years old.")
