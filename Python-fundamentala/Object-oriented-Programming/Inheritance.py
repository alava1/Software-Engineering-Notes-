# inheritance.py
# Topic: Inheritance - Child class inherits from Parent class

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)      # Call parent constructor
        self.color = color
    
    def meow(self):
        print(f"{self.name} says Meow!")
    
    # Overriding parent method
    def eat(self):
        print(f"{self.name} (the {self.color} cat) is eating fish.")

# Another child class
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying high!")

print("=== Inheritance Example ===\n")

cat = Cat("Whiskers", "gray")
bird = Bird("Tweety")

cat.eat()
cat.meow()

bird.eat()
bird.fly()
