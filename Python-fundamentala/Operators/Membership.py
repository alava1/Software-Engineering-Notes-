"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: membership.py

Author: Lawal Yunusa

Description:
This program demonstrates Python membership operators.
Membership operators are used to determine whether a value
exists within a sequence such as a string, list, tuple,
set, or dictionary.

Learning Objectives:
- Understand membership operators
- Use 'in' and 'not in'
- Check membership in different data types
- Apply membership operators in real-world scenarios
=========================================================
"""

# =========================================================
# Introduction
# =========================================================

print("=" * 60)
print("PYTHON MEMBERSHIP OPERATORS")
print("=" * 60)

# =========================================================
# Membership in a List
# =========================================================

languages = ["Python", "Java", "C++", "Go"]

print("\n1. Membership in a List")
print("-" * 60)

print("Languages:", languages)

print("'Python' in languages:", "Python" in languages)
print("'JavaScript' in languages:", "JavaScript" in languages)
print("'Go' not in languages:", "Go" not in languages)

# =========================================================
# Membership in a String
# =========================================================

message = "Python Programming"

print("\n2. Membership in a String")
print("-" * 60)

print("Message:", message)

print("'Python' in message:", "Python" in message)
print("'Java' in message:", "Java" in message)

# =========================================================
# Membership in a Tuple
# =========================================================

numbers = (10, 20, 30, 40)

print("\n3. Membership in a Tuple")
print("-" * 60)

print("Numbers:", numbers)

print("20 in numbers:", 20 in numbers)
print("50 not in numbers:", 50 not in numbers)

# =========================================================
# Membership in a Set
# =========================================================

fruits = {"Apple", "Orange", "Banana"}

print("\n4. Membership in a Set")
print("-" * 60)

print("Fruits:", fruits)

print("'Apple' in fruits:", "Apple" in fruits)
print("'Mango' in fruits:", "Mango" in fruits)

# =========================================================
# Membership in a Dictionary
# =========================================================

student = {
    "name": "Lawal",
    "age": 22,
    "country": "Nigeria"
}

print("\n5. Membership in a Dictionary")
print("-" * 60)

print(student)

print("'name' in student:", "name" in student)
print("'email' in student:", "email" in student)

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

allowed_users = ["admin", "manager", "developer"]

username = "developer"

if username in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Use 'in' to check if an item exists.")
print("✔ Use 'not in' to check if an item does not exist.")
print("✔ Use descriptive variable names.")
print("✔ Choose the appropriate data structure.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("in      -> Returns True if a value exists")
print("not in  -> Returns True if a value does not exist")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
