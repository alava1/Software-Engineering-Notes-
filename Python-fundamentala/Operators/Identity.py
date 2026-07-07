"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: identity.py

Author: Lawal Yunusa

Description:
This program demonstrates Python identity operators.
Identity operators compare whether two variables refer
to the same object in memory, not just whether their
values are equal.

Learning Objectives:
- Understand identity operators
- Learn the difference between 'is' and '=='
- Compare object identity
- Apply identity operators correctly
=========================================================
"""

# =========================================================
# Introduction
# =========================================================

print("=" * 60)
print("PYTHON IDENTITY OPERATORS")
print("=" * 60)

# =========================================================
# Example 1: Comparing Values
# =========================================================

a = 10
b = 10

print("\nExample 1: Integers")

print("a =", a)
print("b =", b)

print("a == b :", a == b)
print("a is b :", a is b)

# =========================================================
# Example 2: Different Lists
# =========================================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("\n" + "=" * 60)
print("Example 2: Different List Objects")
print("=" * 60)

print("list1 =", list1)
print("list2 =", list2)

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)

# =========================================================
# Example 3: Same Object
# =========================================================

list3 = list1

print("\n" + "=" * 60)
print("Example 3: Same Object")
print("=" * 60)

print("list1 == list3 :", list1 == list3)
print("list1 is list3 :", list1 is list3)

# =========================================================
# Identity Operator: is not
# =========================================================

print("\n" + "=" * 60)
print("Identity Operator: is not")
print("=" * 60)

print("list1 is not list2 :", list1 is not list2)
print("list1 is not list3 :", list1 is not list3)

# =========================================================
# Memory Address
# =========================================================

print("\n" + "=" * 60)
print("MEMORY ADDRESS")
print("=" * 60)

print("Address of list1:", id(list1))
print("Address of list2:", id(list2))
print("Address of list3:", id(list3))

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

current_user = None

if current_user is None:
    print("No user is currently logged in.")
else:
    print("User session is active.")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Use == when comparing values.")
print("✔ Use is when comparing object identity.")
print("✔ Use is None to check for None.")
print("✔ Avoid using is with numbers or strings for value comparison.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("is      -> True if both variables reference the same object")
print("is not  -> True if variables reference different objects")
print("==      -> Compares values")
print("id()    -> Returns the memory address of an object")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
