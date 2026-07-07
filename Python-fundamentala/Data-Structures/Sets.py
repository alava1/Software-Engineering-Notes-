# sets.py
# Topic: Sets - Unordered, unique items (no duplicates)

print("=== Sets in Python ===\n")

# Creating sets
numbers = {1, 2, 3, 4, 5, 5, 5}        # Duplicates are removed automatically
print("Set with duplicates removed:", numbers)

fruits = {"apple", "banana", "orange"}
more_fruits = {"banana", "mango", "grapes"}

# Operations
print("\nUnion (combine):", fruits.union(more_fruits))
print("Intersection (common):", fruits.intersection(more_fruits))

# Adding and removing
fruits.add("kiwi")
print("\nAfter adding kiwi:", fruits)

# Sets are very fast for membership testing
if "apple" in fruits:
    print("Apple is in the set!")
