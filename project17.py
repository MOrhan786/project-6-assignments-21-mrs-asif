# 17. Class Decorators
#Assignment:
#Create a class decorator add_greeting that modifies a class to add a greet() method 
#returning "Hello from Decorator!". Apply it to a class Person.

# Class Decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Class to be decorated
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating an instance of the class
person = Person("John")

# Calling the greet method added by the decorator
print(person.greet())
