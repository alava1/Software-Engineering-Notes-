"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: arithmetic.py

Author: Lawal Yunusa

Description:
This program demonstrates Python arithmetic operators.
Arithmetic operators are used to perform mathematical
calculations on numbers.

Learning Objectives:
- Understand arithmetic operators
- Perform mathematical calculations
- Apply operators in real-world scenarios
=========================================================
"""

# =========================================================
# Variables
# =========================================================

a = 20
b = 6

print("=" * 60)
print("PYTHON ARITHMETIC OPERATORS")
print("=" * 60)

print(f"First Number : {a}")
print(f"Second Number: {b}")

# =========================================================
# Addition (+)
# =========================================================

print("\n1. Addition (+)")
addition = a + b
print(f"{a} + {b} = {addition}")

# =========================================================
# Subtraction (-)
# =========================================================

print("\n2. Subtraction (-)")
subtraction = a - b
print(f"{a} - {b} = {subtraction}")

# =========================================================
# Multiplication (*)
# =========================================================

print("\n3. Multiplication (*)")
multiplication = a * b
print(f"{a} * {b} = {multiplication}")

# =========================================================
# Division (/)
# =========================================================

print("\n4. Division (/)")
division = a / b
print(f"{a} / {b} = {division}")

# =========================================================
# Floor Division (//)
# =========================================================

print("\n5. Floor Division (//)")
floor_division = a // b
print(f"{a} // {b} = {floor_division}")

# =========================================================
# Modulus (%)
# =========================================================

print("\n6. Modulus (%)")
remainder = a % b
print(f"{a} % {b} = {remainder}")

# =========================================================
# Exponentiation (**)
# =========================================================

print("\n7. Exponentiation (**)")
power = a ** 2
print(f"{a}² = {power}")

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

price = 2500
quantity = 4

total = price * quantity

print(f"Price per Item : ₦{price}")
print(f"Quantity       : {quantity}")
print(f"Total Cost     : ₦{total}")

# =========================================================
# Operator Precedence
# =========================================================

print("\n" + "=" * 60)
print("OPERATOR PRECEDENCE")
print("=" * 60)

result = 5 + 3 * 2
print("5 + 3 * 2 =", result)

result = (5 + 3) * 2
print("(5 + 3) * 2 =", result)

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Use meaningful variable names.")
print("✔ Use parentheses to improve readability.")
print("✔ Avoid division by zero.")
print("✔ Keep calculations simple and readable.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("+   Addition")
print("-   Subtraction")
print("*   Multiplication")
print("/   Division")
print("//  Floor Division")
print("%   Modulus")
print("**  Exponentiation")

print("\nProgram completed successfully.")
