# OOP Fundamentals Lesson

# OOP is a programming paradigm that models real-world entities as objects. It provides a structure for complex programs by breaking them into smaller, reusable pieces of code.(objects)

# Basic Concepts in OOP:
'''
    - Class: A blueprint for creating objects (blueprint for a house)
    - Object: An instance of a class (the house built from the blueprint)
    - Attributes: Variables that belong to a class (or object). They define the class's properties.
    - Methods: Functions that belong to a class. They define the class's behavior.
'''

# Four Pillars of OOP:
# NOTE: This is a common interview question
'''
    1. Encapsulation: The bundling of attributes and methods that operate inside of a single class.
    2. Inheritance: Where one class (child class) inherits attributes and methods from another class (parent class). This promotes code reusability.
    3. Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface.
    4. Abstraction: Hiding the complexity of the implementation and exposing only the necessary parts.
'''

print("Allan")


# 1. Creating a Classes and Objects
# Creating the class(blueprint)   PascalCase
class MyClass:
    # Constructor
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = 0

    def my_method(self):
        print(f"This is our method. Attribute1: {self.attribute1}. Attribute2: {self.attribute2}.")

# Creating the Object(instance)
obj = MyClass("Allan", "Rahil")
print(obj.attribute2)
obj.my_method()

another_obj = MyClass("Victoria", "Tony")
another_obj.my_method()


# 2. Encapsulation: Implemented by defining instance variables and methods
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Getter funtions
    def get_salary(self):
        return f"This is the salary {self.salary}"

    # Setter Functions
    def set_salary(self, new_salary):
        self.salary = new_salary

employee1 = Employee("Tony", 1000000)
print(employee1.get_salary())

employee1.set_salary(2000000)
print(employee1.get_salary())

employee2 = Employee("Victoria", 250000)
print(employee2.get_salary())

# new_name = input("Enter the name of the new employee")
# new_employee_salary = input("Enter the salary for the new employee")
# new_employee = Employee(new_name, new_employee_salary)
# print(new_employee.get_salary())

# Inheritance: Allows a child class to acquire the properties and behaviors of a parent class
class Animal():
    def breathe(self):
        print('Animal does breathe air')
    
    def speak(self):
        print('Animal makes noise')

class Dog(Animal):
    def speak(self):    #Override the speak function
        print("Dogs BARK!")
    
    def wag_tail(self):
        print("Dog is wagging tail!")

class Cat(Animal):
    def speak(self):
        print('Cats MEOW!')

dog = Dog()
dog.breathe()
dog.speak()
dog.wag_tail()



# Polymorphism: Allows the same method to perform different actions based on the object.
cat = Cat()
cat.breathe()
cat.speak()


# Abstraction: Not seeing the logic that goes into functionality (EX: len(), print(), etc.)
animal = Animal()
animal.breathe()
animal.speak()


print(len([1,2,3]))