# list_methods.py
# Common and useful list methods

numbers = [5, 2, 8, 1, 9, 3]

print("Original:", numbers)

numbers.sort()                    # Sort in ascending order
print("Sorted:", numbers)

numbers.reverse()                 # Reverse the list
print("Reversed:", numbers)

print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# Count occurrences
print("Count of 5:", numbers.count(5))
