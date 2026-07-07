# classes.py
# Topic: Introduction to Classes and Objects

print("=== Object-Oriented Programming ===\n")

# Defining a class
class Dog:
    """This is a Dog class"""
    
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        self.name = name        # Instance attribute
        self.age = age
    
    # Method (function inside class)
    def bark(self):
        print(f"{self.name} says Woof Woof!")
    
    def describe(self):
        print(f"{self.name} is {self.age} years old.")


# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Luna", 5)

print("Dog 1:", dog1.name, "-", dog1.age, "years old")
print("Dog 2:", dog2.name, "-", dog2.age, "years old")

dog1.bark()
dog2.bark()
dog1.describe()
