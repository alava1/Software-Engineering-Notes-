"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: assignment.py

Author: Lawal Yunusa

Description:
This program demonstrates Python assignment operators.
Assignment operators are used to assign values to variables
and update their values efficiently.

Learning Objectives:
- Understand assignment operators
- Assign values to variables
- Update variable values
- Write cleaner and more efficient code
=========================================================
"""

# =========================================================
# Basic Assignment (=)
# =========================================================

print("=" * 60)
print("PYTHON ASSIGNMENT OPERATORS")
print("=" * 60)

number = 20

print("\n1. Basic Assignment (=)")
print("number =", number)

# =========================================================
# Addition Assignment (+=)
# =========================================================

number += 5

print("\n2. Addition Assignment (+=)")
print("number += 5")
print("Result:", number)

# =========================================================
# Subtraction Assignment (-=)
# =========================================================

number -= 3

print("\n3. Subtraction Assignment (-=)")
print("number -= 3")
print("Result:", number)

# =========================================================
# Multiplication Assignment (*=)
# =========================================================

number *= 2

print("\n4. Multiplication Assignment (*=)")
print("number *= 2")
print("Result:", number)

# =========================================================
# Division Assignment (/=)
# =========================================================

number /= 4

print("\n5. Division Assignment (/=)")
print("number /= 4")
print("Result:", number)

# =========================================================
# Floor Division Assignment (//=)
# =========================================================

number //= 2

print("\n6. Floor Division Assignment (//=)")
print("number //= 2")
print("Result:", number)

# =========================================================
# Modulus Assignment (%=)
# =========================================================

number %= 3

print("\n7. Modulus Assignment (%=)")
print("number %= 3")
print("Result:", number)

# =========================================================
# Exponentiation Assignment (**=)
# =========================================================

number = 4

number **= 2

print("\n8. Exponentiation Assignment (**=)")
print("number **= 2")
print("Result:", number)

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

balance = 1000

print("Initial Balance: ₦", balance)

balance += 500
print("Salary Credited: ₦", balance)

balance -= 200
print("Electricity Bill Paid: ₦", balance)

balance -= 150
print("Internet Subscription Paid: ₦", balance)

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Initialize variables before updating them.")
print("✔ Use assignment operators to simplify code.")
print("✔ Use meaningful variable names.")
print("✔ Keep calculations readable.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("=    Assign")
print("+=   Add and Assign")
print("-=   Subtract and Assign")
print("*=   Multiply and Assign")
print("/=   Divide and Assign")
print("//=  Floor Divide and Assign")
print("%=   Modulus and Assign")
print("**=  Exponentiate and Assign")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
