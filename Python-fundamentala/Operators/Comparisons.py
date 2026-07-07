"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: comparison.py

Author: Lawal Yunusa

Description:
This program demonstrates Python comparison operators.
Comparison operators compare two values and always return
a Boolean result: True or False.

Learning Objectives:
- Understand comparison operators
- Compare values
- Interpret Boolean results
- Apply comparisons in decision-making
=========================================================
"""

# =========================================================
# Variables
# =========================================================

a = 15
b = 10

print("=" * 60)
print("PYTHON COMPARISON OPERATORS")
print("=" * 60)

print(f"First Number : {a}")
print(f"Second Number: {b}")

# =========================================================
# Equal To (==)
# =========================================================

print("\n1. Equal To (==)")
print(f"{a} == {b} : {a == b}")

# =========================================================
# Not Equal To (!=)
# =========================================================

print("\n2. Not Equal To (!=)")
print(f"{a} != {b} : {a != b}")

# =========================================================
# Greater Than (>)
# =========================================================

print("\n3. Greater Than (>)")
print(f"{a} > {b} : {a > b}")

# =========================================================
# Less Than (<)
# =========================================================

print("\n4. Less Than (<)")
print(f"{a} < {b} : {a < b}")

# =========================================================
# Greater Than or Equal To (>=)
# =========================================================

print("\n5. Greater Than or Equal To (>=)")
print(f"{a} >= {b} : {a >= b}")

# =========================================================
# Less Than or Equal To (<=)
# =========================================================

print("\n6. Less Than or Equal To (<=)")
print(f"{a} <= {b} : {a <= b}")

# =========================================================
# Comparing Strings
# =========================================================

print("\n" + "=" * 60)
print("STRING COMPARISON")
print("=" * 60)

language1 = "Python"
language2 = "Java"

print(f"{language1} == {language2}: {language1 == language2}")
print(f"{language1} != {language2}: {language1 != language2}")

# =========================================================
# Comparing User Age
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

minimum_age = 18
user_age = 22

print(f"Minimum Age: {minimum_age}")
print(f"User Age: {user_age}")

if user_age >= minimum_age:
    print("Access Granted")
else:
    print("Access Denied")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Use == to compare values.")
print("✔ Do not use = for comparisons.")
print("✔ Write clear comparison expressions.")
print("✔ Test edge cases when comparing values.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("==  Equal To")
print("!=  Not Equal To")
print(">   Greater Than")
print("<   Less Than")
print(">=  Greater Than or Equal To")
print("<=  Less Than or Equal To")

print("\nComparison operators always return True or False.")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
