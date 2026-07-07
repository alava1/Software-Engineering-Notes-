# return_values.py
# Topic: Return Values from Functions

def calculate_rectangle_area(length, width):
    """Calculate and return area"""
    return length * width

def is_even(number):
    """Return True if number is even, False otherwise"""
    return number % 2 == 0

def get_max(a, b, c):
    """Return the largest of three numbers"""
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print("=== Return Values Examples ===\n")

area = calculate_rectangle_area(8, 5)
print(f"Area of rectangle = {area} sq units")

print(f"Is 7 even? {is_even(7)}")
print(f"Is 10 even? {is_even(10)}")

maximum = get_max(45, 78, 23)
print(f"The maximum number is: {maximum}")
