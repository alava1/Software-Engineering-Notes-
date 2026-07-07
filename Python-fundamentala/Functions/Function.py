# functions.py
# Topic: Introduction to Functions

print("=== Functions in Python ===\n")

# A simple function
def greet():
    """This function prints a greeting message"""
    print("Hello, Welcome to Python Fundamentals!")
    print("I hope you're enjoying learning!")

# Calling the function
greet()

print("\n" + "="*40)

# Function with parameters
def greet_user(name, age):
    """Function with parameters"""
    print(f"Hello {name}!")
    print(f"You are {age} years old.")
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

# Calling function with arguments
greet_user("Alice", 22)
print()
greet_user("Bob", 15)
