"""
=========================================================
Python Fundamentals
Chapter 04: Input and Output

File: user_input.py

Author: Lawal Yunusa

Description:
This program demonstrates how to receive user input,
validate it, and handle invalid input using try-except.

Learning Objectives:
- Receive user input
- Validate user input
- Convert input to different data types
- Handle invalid input gracefully
- Build robust interactive programs
=========================================================
"""

# =========================================================
# Program Title
# =========================================================

print("=" * 60)
print("PYTHON USER INPUT")
print("=" * 60)

# =========================================================
# Getting User Information
# =========================================================

print("\nPlease enter your information.")

name = input("Full Name: ")
country = input("Country: ")
profession = input("Profession: ")

# =========================================================
# Age Validation
# =========================================================

while True:
    try:
        age = int(input("Age: "))

        if age < 0:
            print("Age cannot be negative. Try again.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# =========================================================
# Height Validation
# =========================================================

while True:
    try:
        height = float(input("Height (meters): "))

        if height <= 0:
            print("Height must be greater than zero.")
            continue

        break

    except ValueError:
        print("Invalid input. Enter a decimal number.")

# =========================================================
# Display User Information
# =========================================================

print("\n" + "=" * 60)
print("USER PROFILE")
print("=" * 60)

print(f"Name       : {name}")
print(f"Country    : {country}")
print(f"Profession : {profession}")
print(f"Age        : {age}")
print(f"Height     : {height:.2f} m")

# =========================================================
# Age Category
# =========================================================

print("\nAge Category")

if age < 13:
    category = "Child"

elif age < 20:
    category = "Teenager"

elif age < 60:
    category = "Adult"

else:
    category = "Senior Citizen"

print("Category:", category)

# =========================================================
# Greeting
# =========================================================

print("\nWelcome,", name + "!")
print("Thank you for providing your information.")

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Always validate user input.")
print("✔ Use try-except to prevent program crashes.")
print("✔ Give users clear error messages.")
print("✔ Check values before using them.")
print("✔ Keep prompts simple and descriptive.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("input()      -> Receives user input")
print("int()        -> Converts text to integer")
print("float()      -> Converts text to decimal")
print("try-except   -> Handles invalid input")
print("while loop   -> Repeats until valid input is received")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
