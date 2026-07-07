"""
=========================================================
Python Fundamentals
Chapter 04: Input and Output

File: input_output.py

Author: Lawal Yunusa

Description:
This program demonstrates the basics of input and output
in Python. It shows how to display information using the
print() function and receive information from users using
the input() function.

Learning Objectives:
- Understand input and output
- Display text using print()
- Receive user input
- Store user input in variables
- Display user information
=========================================================
"""

# =========================================================
# Program Title
# =========================================================

print("=" * 60)
print("PYTHON INPUT AND OUTPUT")
print("=" * 60)

# =========================================================
# Output Example
# =========================================================

print("\nExample 1: Displaying Output")

print("Hello, World!")
print("Welcome to Python Fundamentals.")
print("Python makes it easy to build amazing software.")

# =========================================================
# Receiving User Input
# =========================================================

print("\nExample 2: Receiving User Input")

name = input("Enter your name: ")

# =========================================================
# Display User Input
# =========================================================

print("\nHello,", name + "!")
print("Welcome to this Python lesson.")

# =========================================================
# Multiple Inputs
# =========================================================

print("\nExample 3: Multiple User Inputs")

city = input("Enter your city: ")
country = input("Enter your country: ")

print("\nLocation Information")
print("------------------------------")
print("City    :", city)
print("Country :", country)

# =========================================================
# Numeric Input
# =========================================================

print("\nExample 4: Numeric Input")

age = int(input("Enter your age: "))

print(f"You are {age} years old.")

# =========================================================
# Simple Calculation
# =========================================================

next_year = age + 1

print(f"Next year you will be {next_year} years old.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("print()  -> Displays output")
print("input()  -> Receives user input")
print("int()    -> Converts text to an integer")
print("Variables store user information.")

# =========================================================
# Best Practices
# =========================================================

print("\nBest Practices")

print("- Write clear prompts for users.")
print("- Validate user input.")
print("- Convert data types when necessary.")
print("- Keep output clean and readable.")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
