# multiplication_table.py
# Topic: Practical Project - Multiplication Table

print("=== Multiplication Table Generator ===\n")

try:
    number = int(input("Enter a number to see its multiplication table: "))
    limit = int(input("Up to what number? (e.g. 10): "))

    print(f"\nMultiplication Table of {number} (up to {limit}):")
    print("-" * 30)
    
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} × {i:2} = {result:3}")
        
except ValueError:
    print("❌ Please enter valid numbers!")
