"""
=========================================================
Python Fundamentals
Chapter 05: Conditional Statements

File: if_else.py

Author: Lawal Yunusa

Description:
This program demonstrates the Python if...else statement.
The if...else statement allows a program to choose between
two possible actions depending on whether a condition is
True or False.

Learning Objectives:
- Understand the if...else statement
- Make two-way decisions
- Execute different code blocks
- Apply if...else in real-world programs
=========================================================
"""

# =========================================================
# Program Title
# =========================================================

print("=" * 60)
print("PYTHON IF...ELSE STATEMENT")
print("=" * 60)

# =========================================================
# Example 1: Even or Odd Number
# =========================================================

print("\nExample 1: Even or Odd Number")

number = 18

print("Number:", number)

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# =========================================================
# Example 2: Voting Eligibility
# =========================================================

print("\n" + "=" * 60)
print("Example 2: Voting Eligibility")
print("=" * 60)

age = 16

print("Age:", age)

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# =========================================================
# Example 3: Login Authentication
# =========================================================

print("\n" + "=" * 60)
print("Example 3: Login Authentication")
print("=" * 60)

username = "admin"
password = "Python123"

if username == "admin" and password == "Python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")

# =========================================================
# Example 4: Pass or Fail
# =========================================================

print("\n" + "=" * 60)
print("Example 4: Student Result")
print("=" * 60)

score = 45

print("Score:", score)

if score >= 50:
    print("Congratulations! You passed.")
else:
    print("Sorry! You failed.")

# =========================================================
# Example 5: Bank Withdrawal
# =========================================================

print("\n" + "=" * 60)
print("Example 5: Bank Withdrawal")
print("=" * 60)

balance = 5000
withdraw_amount = 7000

print("Account Balance :", balance)
print("Withdrawal      :", withdraw_amount)

if withdraw_amount <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

temperature = 32

if temperature > 30:
    print("Weather: Hot")
else:
    print("Weather: Cool")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Keep conditions readable.")
print("✔ Indent code correctly.")
print("✔ Use meaningful variable names.")
print("✔ Avoid unnecessary nesting.")
print("✔ Test both True and False cases.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("if    -> Executes when condition is True")
print("else  -> Executes when condition is False")
print("Exactly one block executes.")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
