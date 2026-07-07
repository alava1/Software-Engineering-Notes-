# polymorphism.py
# Topic: Polymorphism - Same method name, different behavior

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

print("=== Polymorphism Example ===\n")

shapes = [
    Rectangle(5, 3),
    Circle(4)
]

for shape in shapes:
    print(f"Area = {shape.area()}")
