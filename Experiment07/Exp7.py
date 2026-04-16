# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)


# Derived Class
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def show_student(self):
        self.show_person()
        print("Marks:", self.marks)

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def result(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"


# Creating Objects
s1 = Student("ZAY", 20, 85)
s2 = Student("ANNA", 19, 92)

# Student 1 Details
print("\nStudent 1 Details")
s1.show_student()
print("Grade :", s1.grade())
print("Result:", s1.result())

# Student 2 Details
print("\nStudent 2 Details")
s2.show_student()
print("Grade :", s2.grade())
print("Result:", s2.result())
