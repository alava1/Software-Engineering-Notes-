"""
=========================================================
Python Fundamentals
Chapter 01: Getting Started

File: first_program.py

Author: Lawal Yunusa

Description:
This is a simple interactive Python program. It asks the
user for their name and age, then displays a personalized
welcome message.

This example introduces:
- Variables
- User input
- Output
- Type conversion
- Formatted strings (f-strings)
=========================================================
"""

# ---------------------------------------------------------
# Welcome Message
# ---------------------------------------------------------

print("=" * 50)
print("      Welcome to Python Fundamentals")
print("=" * 50)

# ---------------------------------------------------------
# Get User Information
# ---------------------------------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print("\nHello,", name + "!")
print(f"You are {age} years old.")

# ---------------------------------------------------------
# Simple Age Check
# ---------------------------------------------------------

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ---------------------------------------------------------
# Motivational Message
# ---------------------------------------------------------

print("\nKeep learning Python every day!")
print("Practice consistently and build amazing projects.")

# ---------------------------------------------------------
# Goodbye Message
# ---------------------------------------------------------

print("\nThank you for using this program.")
print("See you in the next lesson!")

print("=" * 50)
