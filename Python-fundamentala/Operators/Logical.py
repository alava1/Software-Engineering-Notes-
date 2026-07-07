"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: logical.py

Author: Lawal Yunusa

Description:
This program demonstrates Python logical operators.
Logical operators are used to combine multiple conditions
and return either True or False.

Learning Objectives:
- Understand logical operators
- Combine multiple conditions
- Make decisions based on Boolean expressions
- Apply logical operators in real-world programs
=========================================================
"""

# =========================================================
# Variables
# =========================================================

age = 22
has_id = True
has_ticket = False

print("=" * 60)
print("PYTHON LOGICAL OPERATORS")
print("=" * 60)

print(f"Age       : {age}")
print(f"Has ID    : {has_id}")
print(f"Has Ticket: {has_ticket}")

# =========================================================
# Logical AND
# =========================================================

print("\n1. Logical AND (and)")
print("-" * 60)

print("Age >= 18 and Has ID")
print(age >= 18 and has_id)

# =========================================================
# Logical OR
# =========================================================

print("\n2. Logical OR (or)")
print("-" * 60)

print("Has ID or Has Ticket")
print(has_id or has_ticket)

# =========================================================
# Logical NOT
# =========================================================

print("\n3. Logical NOT (not)")
print("-" * 60)

print("not Has Ticket")
print(not has_ticket)

# =========================================================
# Real-World Example 1
# =========================================================

print("\n" + "=" * 60)
print("LOGIN VERIFICATION")
print("=" * 60)

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# =========================================================
# Real-World Example 2
# =========================================================

print("\n" + "=" * 60)
print("UNIVERSITY ADMISSION")
print("=" * 60)

score = 75
passed_interview = True

if score >= 60 and passed_interview:
    print("Admission Approved")
else:
    print("Admission Denied")

# =========================================================
# Real-World Example 3
# =========================================================

print("\n" + "=" * 60)
print("EVENT ENTRY")
print("=" * 60)

if age >= 18 and has_ticket:
    print("Entry Allowed")
else:
    print("Entry Denied")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Keep logical expressions simple.")
print("✔ Use parentheses for readability.")
print("✔ Test each condition separately.")
print("✔ Avoid deeply nested conditions.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("and  -> Returns True if both conditions are True")
print("or   -> Returns True if at least one condition is True")
print("not  -> Reverses the Boolean value")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
