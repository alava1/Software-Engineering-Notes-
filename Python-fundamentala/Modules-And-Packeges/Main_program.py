# main_program.py
# Topic: Importing and Using Modules

# Import specific functions
from custom_module import greet, add

# Import with alias
import math as m

print("=== Working with Modules ===\n")

# Using imported functions
print(greet("Oluwaseun"))
print("Sum:", add(15, 27))

# Using math module with alias
print("Square root of 49:", m.sqrt(49))
print("Value of Pi:", m.pi)

# Import everything (not recommended for large projects)
import random
print("Random number:", random.randint(10, 50))
