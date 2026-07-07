# parameters.py
# Topic: Function Parameters & Arguments

def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

def multiply_numbers(x, y=2):
    """Function with default parameter"""
    return x * y

print("=== Function Parameters Demo ===\n")

# Using return values
sum_result = add_numbers(10, 25)
print(f"10 + 25 = {sum_result}")

# Using default parameter
print(f"5 * 2 (default) = {multiply_numbers(5)}")
print(f"5 * 8 = {multiply_numbers(5, 8)}")

print("\n" + "="*40)

# Keyword arguments
def describe_person(name, age, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

describe_person(name="John", age=30, city="Lagos")
