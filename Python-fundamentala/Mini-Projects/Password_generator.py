# password_generator.py
# Project: Random Password Generator

import random
import string

print("=== Password Generator ===\n")

length = int(input("Enter password length (recommended 12+): "))

# Define character sets
letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Combine all characters
all_characters = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_characters) for _ in range(length))

print(f"\nYour generated password: {password}")
print(f"Length: {length} characters")
