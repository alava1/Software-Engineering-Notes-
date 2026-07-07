"""
=========================================================
Python Fundamentals
Chapter 02: Variables and Data Types

File: type_conversion.py

Author: Lawal Yunusa

Description:
This program demonstrates type conversion (also called type
casting) in Python. Type conversion allows developers to
convert data from one type to another when needed.

Learning Objectives:
- Understand type conversion
- Convert between common data types
- Identify implicit and explicit conversion
- Avoid common conversion errors
=========================================================
"""

# =========================================================
# What is Type Conversion?
# =========================================================

print("=" * 60)
print("PYTHON TYPE CONVERSION")
print("=" * 60)

print("\nType conversion changes a value from one data type")
print("to another.")

# =========================================================
# Integer to Float
# =========================================================

age = 22

print("\n1. Integer to Float")
print("Original:", age, type(age))

age_float = float(age)

print("Converted:", age_float, type(age_float))

# =========================================================
# Float to Integer
# =========================================================

price = 49.99

print("\n2. Float to Integer")
print("Original:", price, type(price))

price_int = int(price)

print("Converted:", price_int, type(price_int))

# =========================================================
# Integer to String
# =========================================================

number = 100

print("\n3. Integer to String")
print("Original:", number, type(number))

number_str = str(number)

print("Converted:", number_str, type(number_str))

# =========================================================
# String to Integer
# =========================================================

marks = "95"

print("\n4. String to Integer")
print("Original:", marks, type(marks))

marks_int = int(marks)

print("Converted:", marks_int, type(marks_int))

# =========================================================
# String to Float
# =========================================================

weight = "72.5"

print("\n5. String to Float")
print("Original:", weight, type(weight))

weight_float = float(weight)

print("Converted:", weight_float, type(weight_float))

# =========================================================
# Boolean Conversion
# =========================================================

print("\n6. Boolean Conversion")

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2, 3]))

# =========================================================
# List to Tuple
# =========================================================

languages = ["Python", "Java", "C++"]

print("\n7. List to Tuple")

languages_tuple = tuple(languages)

print(languages_tuple)
print(type(languages_tuple))

# =========================================================
# Tuple to List
# =========================================================

numbers = (10, 20, 30)

print("\n8. Tuple to List")

numbers_list = list(numbers)

print(numbers_list)
print(type(numbers_list))

# =========================================================
# Implicit Type Conversion
# =========================================================

print("\n9. Implicit Type Conversion")

result = 10 + 5.5

print(result)
print(type(result))

# =========================================================
# Common Conversion Error
# =========================================================

print("\n10. Handling Conversion Errors")

value = "Hello"

try:
    number = int(value)
except ValueError:
    print("Cannot convert 'Hello' to an integer.")

# =========================================================
# Best Practices
# =========================================================

print("\nBest Practices")

print("- Validate user input before converting.")
print("- Use try-except when converting unknown values.")
print("- Avoid unnecessary conversions.")
print("- Understand data loss when converting floats to integers.")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
