# class Student(self , name , marks):
#     name  = self.name
#     marks = self.marks

# 1. Using self 
class Student :
    def __init__(self , name , marks):
        self.name = name 
        self.marks = marks
    
    def display(self):
        print(f"student name is {self.name } and gain marks is {self.marks}")


student1 = Student("usman" , 100)
# student1.display()

# 2. Using cls

class Counter:
    count = 0


    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_obj(cls):
        print(f"total no. of objects created {cls.count}")


# 3. Public Variables and Methods


class Car:
    def __init__(self , brands):
        self.brands = brands
    
    def start(self):
        print(f"{self.brands} car has started")

my_car = Car("Toyota")
# print(my_car.brands)
# my_car.start()

# 4. Class Variables and Class Methods


class Bank:
    bank_name = "al-habib-bank"


    @classmethod
    def change_bank_name(cls , name):
        cls.bank_name = name

customer1 = Bank()
customer2 = Bank()

# print(customer1.bank_name)
# print(customer2.bank_name)

# Bank.change_bank_name("meezan bank")

# print(customer1.bank_name)
# print(customer2.bank_name)

# 5. Static Variables and Static Methods

class MathUtils:
    

    @staticmethod
    def add(a , b):
        return a + b
    
# result = MathUtils.add(3, 5)
# print(result)

# 6. Constructors and Destructors


class Logger :

    def __init__(self):
        print("new object is created")
    def __del__(self):
        print(" object is delete")

log = Logger()
del log

# 7. Access Modifiers: Public, Private, and Protected

