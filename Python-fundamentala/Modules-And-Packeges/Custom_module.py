# custom_module.py
# This is a custom module that we will import

def greet(name):
    """Greet the user"""
    return f"Hello, {name}! Welcome to Python."

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

# This code runs only when the file is executed directly
if __name__ == "__main__":
    print("This module is being run directly!")
    print(greet("Student"))
    print("5 + 3 =", add(5, 3))
else:
    print("custom_module has been imported!")
