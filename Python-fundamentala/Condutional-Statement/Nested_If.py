# nested_if.py
# Topic: Nested if statements (if inside another if)

print("=== Nested If Statements ===\n")

age = 25
has_license = True

print(f"Age: {age}, Has Driver's License: {has_license}")

if age >= 18:
    print("You are an adult.")
    
    # Nested if - only checked if outer condition is True
    if has_license:
        print("✅ You can drive a car legally.")
    else:
        print("❌ You need to get a driver's license first.")
else:
    print("You are still a minor.")

print("\nNote: Nested ifs are useful but can become complex.")
