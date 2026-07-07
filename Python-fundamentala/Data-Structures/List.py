# lists.py
# Topic: Lists - Ordered, mutable (changeable) collection

print("=== Lists in Python ===\n")

# Creating a list
fruits = ["apple", "banana", "orange", "mango", "pineapple"]

print("Original list:", fruits)
print("Number of fruits:", len(fruits))
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding items
fruits.append("grapes")           # Add to the end
print("\nAfter append:", fruits)

fruits.insert(2, "kiwi")          # Insert at specific position
print("After insert:", fruits)

# Removing items
fruits.remove("banana")           # Remove by value
print("After remove:", fruits)

popped = fruits.pop()             # Remove and return last item
print(f"Popped item: {popped}")
print("After pop:", fruits)

# Slicing
print("\nFirst 3 fruits:", fruits[:3])
print("Last 2 fruits:", fruits[-2:])
