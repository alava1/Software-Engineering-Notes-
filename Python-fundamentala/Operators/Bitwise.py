"""
=========================================================
Python Fundamentals
Chapter 03: Operators

File: bitwise.py

Author: Lawal Yunusa

Description:
This program demonstrates Python bitwise operators.
Bitwise operators perform operations directly on the
binary representation of integers.

Learning Objectives:
- Understand bitwise operators
- Perform binary operations
- Learn practical use cases
- Interpret binary results
=========================================================
"""

# =========================================================
# Variables
# =========================================================

a = 10      # Binary: 1010
b = 4       # Binary: 0100

print("=" * 60)
print("PYTHON BITWISE OPERATORS")
print("=" * 60)

print(f"a = {a} (Binary: {bin(a)})")
print(f"b = {b} (Binary: {bin(b)})")

# =========================================================
# Bitwise AND (&)
# =========================================================

print("\n1. Bitwise AND (&)")
result = a & b
print(f"{a} & {b} = {result}")
print("Binary:", bin(result))

# =========================================================
# Bitwise OR (|)
# =========================================================

print("\n2. Bitwise OR (|)")
result = a | b
print(f"{a} | {b} = {result}")
print("Binary:", bin(result))

# =========================================================
# Bitwise XOR (^)
# =========================================================

print("\n3. Bitwise XOR (^)")
result = a ^ b
print(f"{a} ^ {b} = {result}")
print("Binary:", bin(result))

# =========================================================
# Bitwise NOT (~)
# =========================================================

print("\n4. Bitwise NOT (~)")
result = ~a
print(f"~{a} = {result}")

# =========================================================
# Left Shift (<<)
# =========================================================

print("\n5. Left Shift (<<)")
result = a << 2
print(f"{a} << 2 = {result}")
print("Binary:", bin(result))

# =========================================================
# Right Shift (>>)
# =========================================================

print("\n6. Right Shift (>>)")
result = a >> 2
print(f"{a} >> 2 = {result}")
print("Binary:", bin(result))

# =========================================================
# Real-World Example
# =========================================================

print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE")
print("=" * 60)

READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

user_permission = READ | WRITE

print("User Permission Value:", user_permission)

print("Can Read   :", bool(user_permission & READ))
print("Can Write  :", bool(user_permission & WRITE))
print("Can Execute:", bool(user_permission & EXECUTE))

# =========================================================
# Best Practices
# =========================================================

print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("✔ Understand binary numbers before using bitwise operators.")
print("✔ Use descriptive constant names for bit masks.")
print("✔ Document bitwise operations in your code.")
print("✔ Test bitwise expressions carefully.")

# =========================================================
# Summary
# =========================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("&   Bitwise AND")
print("|   Bitwise OR")
print("^   Bitwise XOR")
print("~   Bitwise NOT")
print("<<  Left Shift")
print(">>  Right Shift")

# =========================================================
# End of Program
# =========================================================

print("\nProgram completed successfully.")
