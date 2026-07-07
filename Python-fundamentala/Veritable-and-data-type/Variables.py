"""
=========================================================
Python Fundamentals
Chapter 02: Variables and Data Types

File: variables.py

Author: Lawal Yunusa

Description:
This program introduces variables in Python. Variables are
used to store data that can be used and modified throughout
a program.

Learning Objectives:
- Understand what variables are
- Create variables
- Assign values to variables
- Display variable values
- Follow Python naming conventions
=========================================================
"""

# ---------------------------------------------------------
# What is a Variable?
# ---------------------------------------------------------

# A variable is a named location in memory used to store data.

name = "Lawal Yunusa"
age = 22
country = "Nigeria"

# ---------------------------------------------------------
# Display Variables
# ---------------------------------------------------------

print("Name:", name)
print("Age:", age)
print("Country:", country)

# ---------------------------------------------------------
# Updating Variables
# ---------------------------------------------------------

print("\nUpdating age...")

age = 23

print("New Age:", age)

# ---------------------------------------------------------
# Multiple Variable Assignment
# ---------------------------------------------------------

x, y, z = 10, 20, 30

print("\nMultiple Assignment")
print("x =", x)
print("y =", y)
print("z =", z)

# ---------------------------------------------------------
# Assign Same Value to Multiple Variables
# ---------------------------------------------------------

python = java = csharp = "Programming Language"

print("\nSame Value Assignment")
print("Python:", python)
print("Java:", java)
print("C#:", csharp)

# ---------------------------------------------------------
# Variable Naming Examples
# ---------------------------------------------------------

student_name = "Amina"
student_age = 21
is_graduated = False

print("\nStudent Information")
print("Name:", student_name)
print("Age:", student_age)
print("Graduated:", is_graduated)

# ---------------------------------------------------------
# Best Practices
# ---------------------------------------------------------

print("\nBest Practices for Variables")
print("- Use meaningful names")
print("- Use snake_case naming")
print("- Avoid reserved keywords")
print("- Keep names short but descriptive")

# ---------------------------------------------------------
# End of Program
# ---------------------------------------------------------

print("\nProgram completed successfully.")
