"""
=========================================================
Python Fundamentals
Chapter 02: Variables and Data Types

File: data_types.py

Author: Lawal Yunusa

Description:
This program introduces Python's built-in data types.
Understanding data types is essential because every value
stored in a program belongs to a specific type.

Learning Objectives:
- Understand Python data types
- Create different data types
- Check data types using type()
- Learn when to use each data type
=========================================================
"""

# ---------------------------------------------------------
# String (str)
# ---------------------------------------------------------

name = "Lawal Yunusa"

print("=" * 60)
print("STRING")
print("=" * 60)

print("Value:", name)
print("Data Type:", type(name))

# ---------------------------------------------------------
# Integer (int)
# ---------------------------------------------------------

age = 22

print("\n" + "=" * 60)
print("INTEGER")
print("=" * 60)

print("Value:", age)
print("Data Type:", type(age))

# ---------------------------------------------------------
# Float (float)
# ---------------------------------------------------------

height = 1.75

print("\n" + "=" * 60)
print("FLOAT")
print("=" * 60)

print("Value:", height)
print("Data Type:", type(height))

# ---------------------------------------------------------
# Boolean (bool)
# ---------------------------------------------------------

is_student = True

print("\n" + "=" * 60)
print("BOOLEAN")
print("=" * 60)

print("Value:", is_student)
print("Data Type:", type(is_student))

# ---------------------------------------------------------
# List (list)
# ---------------------------------------------------------

languages = ["Python", "Java", "C++", "Go"]

print("\n" + "=" * 60)
print("LIST")
print("=" * 60)

print("Value:", languages)
print("Data Type:", type(languages))

# ---------------------------------------------------------
# Tuple (tuple)
# ---------------------------------------------------------

coordinates = (10, 20)

print("\n" + "=" * 60)
print("TUPLE")
print("=" * 60)

print("Value:", coordinates)
print("Data Type:", type(coordinates))

# ---------------------------------------------------------
# Set (set)
# ---------------------------------------------------------

numbers = {1, 2, 3, 4, 5}

print("\n" + "=" * 60)
print("SET")
print("=" * 60)

print("Value:", numbers)
print("Data Type:", type(numbers))

# ---------------------------------------------------------
# Dictionary (dict)
# ---------------------------------------------------------

student = {
    "name": "Lawal",
    "age": 22,
    "country": "Nigeria"
}

print("\n" + "=" * 60)
print("DICTIONARY")
print("=" * 60)

print("Value:", student)
print("Data Type:", type(student))

# ---------------------------------------------------------
# NoneType
# ---------------------------------------------------------

result = None

print("\n" + "=" * 60)
print("NONE TYPE")
print("=" * 60)

print("Value:", result)
print("Data Type:", type(result))

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("SUMMARY OF PYTHON DATA TYPES")
print("=" * 60)

print("str   -> Text")
print("int   -> Whole Numbers")
print("float -> Decimal Numbers")
print("bool  -> True or False")
print("list  -> Ordered Collection")
print("tuple -> Immutable Collection")
print("set   -> Unique Values")
print("dict  -> Key-Value Pairs")
print("None  -> Represents No Value")

print("\nProgram completed successfully.")
