# for_loop.py
# Topic: For Loops - Used when you know how many times to repeat

print("=== For Loop Examples ===\n")

# Example 1: Looping through a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):        # range(start, stop) - stops before 6
    print(f"Number: {i}")

print("\n" + "="*30)

# Example 2: Looping through a list
fruits = ["apple", "banana", "cherry", "mango"]

print("My favorite fruits:")
for fruit in fruits:
    print(f"→ {fruit}")

print("\n" + "="*30)

# Example 3: Using range with step
print("Even numbers between 2 and 10:")
for num in range(2, 11, 2):   # start=2, stop=11, step=2
    print(num)
