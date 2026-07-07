"""
=========================================================
Python Fundamentals
Chapter 02: Variables and Data Types

File: constants.py

Author: Lawal Yunusa

Description:
This program demonstrates how constants are represented
in Python. Although Python does not enforce true constants,
developers use naming conventions to indicate values that
should not change throughout a program.

Learning Objectives:
- Understand what constants are
- Learn Python constant naming conventions
- Use constants in calculations
- Follow best coding practices
=========================================================
"""

# =========================================================
# What is a Constant?
# =========================================================

print("=" * 60)
print("PYTHON CONSTANTS")
print("=" * 60)

print("\nA constant is a value that should remain unchanged")
print("during the execution of a program.")

print("\nPython does not have built-in constants.")
print("Instead, programmers use UPPERCASE names.")

# =========================================================
# Defining Constants
# =========================================================

PI = 3.1415926535
GRAVITY = 9.81
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

# =========================================================
# Display Constants
# =========================================================

print("\nDefined Constants")
print("-" * 60)

print("PI =", PI)
print("GRAVITY =", GRAVITY)
print("SECONDS_PER_MINUTE =", SECONDS_PER_MINUTE)
print("MINUTES_PER_HOUR =", MINUTES_PER_HOUR)
print("HOURS_PER_DAY =", HOURS_PER_DAY)

# =========================================================
# Example 1: Area of a Circle
# =========================================================

radius = 7

area = PI * radius ** 2

print("\nArea of a Circle")
print("-" * 60)

print("Radius:", radius)
print("Area:", area)

# =========================================================
# Example 2: Time Conversion
# =========================================================

days = 2

seconds = (
    days *
    HOURS_PER_DAY *
    MINUTES_PER_HOUR *
    SECONDS_PER_MINUTE
)

print("\nTime Conversion")
print("-" * 60)

print(days, "days =", seconds, "seconds")

# =========================================================
# Example 3: Weight Calculation
# =========================================================

mass = 70

weight = mass * GRAVITY

print("\nWeight Calculation")
print("-" * 60)

print("Mass:", mass, "kg")
print("Weight:", weight, "N")

# =========================================================
# Constant Naming Convention
# =========================================================

print("\nNaming Convention")
print("-" * 60)

print("✔ PI")
print("✔ MAX_USERS")
print("✔ API_URL")
print("✔ TAX_RATE")
print("✔ SPEED_OF_LIGHT")

# =========================================================
# Best Practices
# =========================================================

print("\nBest Practices")
print("-" * 60)

print("• Use UPPERCASE names for constants.")
print("• Keep constant names descriptive.")
print("• Define constants at the top of the file.")
print("• Avoid changing constant values.")
print("• Group related constants together.")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
