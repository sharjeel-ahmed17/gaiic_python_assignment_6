# class Student(self , name , marks):
#     name  = self.name
#     marks = self.marks

# assignment 1 
class Student :
    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks
    
    def display(self):
        print(f"student name is {self.name } and gain marks is {self.marks}")


student1 = Student("usman" , 100)
student1.display()

# assignment 2

class Counter:
    pass
