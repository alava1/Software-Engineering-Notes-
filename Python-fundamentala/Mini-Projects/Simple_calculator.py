# simple_calculator.py
# Project: Simple Interactive Calculator

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0: return "Error: Division by zero!"
    return x / y

print("=== Simple Calculator ===\n")

while True:
    print("\nOperations: +, -, *, /")
    print("Type 'quit' to exit.")
    
    choice = input("\nEnter operation: ")
    
    if choice.lower() == 'quit':
        print("Goodbye!")
        break
    
    if choice in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '+':
                print(f"Result: {add(num1, num2)}")
            elif choice == '-':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '*':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '/':
                print(f"Result: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numbers.")
    else:
        print("Invalid operation!")
