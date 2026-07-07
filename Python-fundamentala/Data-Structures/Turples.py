# tuples.py
# Topic: Tuples - Ordered, immutable (cannot change) collection

print("=== Tuples in Python ===\n")

# Creating a tuple
coordinates = (10, 20)
colors = ("red", "green", "blue")
person = ("Alice", 25, "Lagos")

print("Coordinates:", coordinates)
print("Colors:", colors)

# Tuples are immutable - this would cause an error:
# colors[0] = "yellow"   # Not allowed!

# Useful operations
print("\nNumber of colors:", len(colors))
print("First color:", colors[0])

# Unpacking a tuple
name, age, city = person
print(f"\nUnpacked -> Name: {name}, Age: {age}, City: {city}")
