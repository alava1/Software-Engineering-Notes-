"""
=========================================================
Python Fundamentals
Chapter 05: Conditional Statements

File: if_statement.py

Author: Lawal Yunusa

Description:
This program demonstrates the use of Python's 'if'
statement. An 'if' statement executes a block of code
only when a specified condition evaluates to True.

Learning Objectives:
- Understand the if statement
- Evaluate Boolean expressions
- Execute code conditionally
- Build simple decision-making programs
=========================================================
"""

# =========================================================
# Program Title
# =========================================================

print("=" * 60)
print("PYTHON IF STATEMENT")
print("=" * 60)

# =========================================================
# Example 1: Positive Number
# =========================================================

print("\nExample 1: Positive Number")

number = 15

print("Number:", number)

if number > 0:
    print("The number is positive.")

# =========================================================
# Example 2: Voting Eligibility
# =========================================================

print("\n" + "=" * 60)
print("Example 2: Voting Eligibility")
print("=" * 60)

age = 20

print("Age:", age)

if age >= 18:
    print("You are eligible to vote.")

# =========================================================
# Example 3: Password Length
# =========================================================

print("\n" + "=" * 60)
print("Example 3: Password Validation")
print("=" * 60)

password = "Python123"

print("Password:", password)

if len(password) >= 8:
    print("Password length is acceptable.")

# =========================================================
# Example 4: Student Pass Check
# =========================================================

print("\n" + "=" * 60)
print("Example 4: Student Result")
print("=" * 60)

score = 75

print("Score:", score)

if score >= 50:
    print("Congratulations! You passed the examination.")

# =========================================================
# Example 5: Bank Account Balance
# =========================================================

print("\n" + "=" * 60)
print("Example 5: Bank Account")
print("=" * 60)

balance = 25000

print("Account Balance: ₦", balance)

if balance > 0:
    print("Your account has available funds.")

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

logged_in = True

if logged_in:
    print("Welcome back!")
    print("Access granted to the dashboard.")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Keep conditions simple.")
print("✔ Use meaningful variable names.")
print("✔ Indent code correctly.")
print("✔ Avoid unnecessary conditions.")
print("✔ Test different scenarios.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("if statement executes code only when a condition is True.")
print("Conditions evaluate to either True or False.")
print("Indentation defines the code block.")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
