# while_loop.py
# Topic: While Loops - Repeat as long as a condition is True

print("=== While Loop Examples ===\n")

# Example 1: Simple counter
count = 1

print("Counting with while loop:")
while count <= 5:
    print(f"Count: {count}")
    count += 1          # Important: Increment to avoid infinite loop!

print("\n" + "="*30)

# Example 2: User input validation
print("Password Checker (demo)")

password = ""
attempts = 0

while password != "python123" and attempts < 3:
    password = input("Enter password: ")
    attempts += 1
    
    if password == "python123":
        print("✅ Access Granted! Welcome.")
    elif attempts < 3:
        print(f"❌ Wrong password. {3 - attempts} attempt(s) left.")
    else:
        print("❌ Too many failed attempts. Access denied.")
