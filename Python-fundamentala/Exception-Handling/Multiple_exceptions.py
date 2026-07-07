# multiple_exceptions.py
# Topic: Handling Multiple Exceptions

print("=== Multiple Exception Handling ===\n")

def safe_divide(a, b):
    try:
        result = a / b
        print(f"{a} ÷ {b} = {result}")
        return result
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# Test cases
safe_divide(10, 2)
safe_divide(10, 0)        # ZeroDivisionError
safe_divide(10, "five")   # TypeError
