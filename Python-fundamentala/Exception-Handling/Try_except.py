# try_except.py
# Topic: Basic Exception Handling with try...except

print("=== Exception Handling ===\n")

# Example 1: Handling division by zero
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")
    
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")
    
except ValueError:
    print("❌ Error: Please enter valid numbers!")

except Exception as e:          # Catch any other error
    print(f"❌ An unexpected error occurred: {e}")
