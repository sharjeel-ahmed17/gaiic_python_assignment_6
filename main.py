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

# log = Logger()
# del log

# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         
        self._salary = salary    
        self.__ssn = ssn         

emp = Employee("Alice", 70000, "123-45-6789")


# print("Public: ", emp.name)            
# print("Protected: ", emp._salary)      
# try:
#     print("Private: ", emp.__ssn)      
# except AttributeError as e:
#     print("Private: Cannot access directly -", e)

# # Accessing private variable using name mangling
# print("Private (via name mangling):", emp._Employee__ssn)


# 8. The super() Function


class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)      # Call the constructor of Person
        self.subject = subject

# Creating an object of Teacher
t = Teacher("John Smith", "Mathematics")

# Accessing attributes
# print("Name:", t.name)
# print("Subject:", t.subject)



# 9

from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass implementing the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Trying to instantiate Shape will raise an error
# s = Shape()  # This will raise TypeError

# Create a Rectangle object and compute area
r = Rectangle(10, 5)
# print("Area of rectangle:", r.area())


#10 

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Example usage
d = Dog("Buddy", "Golden Retriever")
# d.bark()

# 11
class Book:
    total_books = 0  # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment count when a book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Create some Book objects
b1 = Book("1984", "George Orwell")
b2 = Book("To Kill a Mockingbird", "Harper Lee")

# Access the class variable
# print("Total books created:", Book.total_books)


#12

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
# print(f"{temp_c}°C is {temp_f}°F")

# 13
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        return self.engine.start()  # Access Engine's method via Car

# Create an Engine object
engine = Engine()

# Pass Engine object to Car
car = Car(engine)

# Start the car
# print(car.start_car())

#14

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: holds reference to an existing Employee object

    def show_employee(self):
        return f"Department: {self.dept_name} | {self.employee.get_details()}"

# Create an Employee object independently
emp = Employee("Alice", 101)

# Create a Department object that aggregates the Employee
dept = Department("HR", emp)

# Display information
# print(dept.show_employee())

# 15


class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):  # Multiple inheritance
    pass

# Create object of class D
d = D()
# d.show()  # Observe MRO

# Print the method resolution order
# print(D.__mro__)

# 16

# Decorator definition
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
# say_hello()


# 17

# Class decorator definition
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Usage
p = Person("Alice")
# print(p.greet())


# 18

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute by convention

    @property
    def price(self):
        """Get the price"""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price, with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price"""
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)
# print(p.price)    # Get price

# p.price = 150     # Set price
# print(p.price)

# del p.price       # Delete price
# print(p.price)  # This will raise AttributeError because _price no longer exists
