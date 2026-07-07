# ⚠️ Chapter 11: Exception Handling

## 📖 Introduction

Exception handling is the process of detecting and responding to runtime errors so that a program can continue running or fail gracefully instead of crashing unexpectedly.

Errors can occur for many reasons, such as invalid user input, missing files, network failures, or division by zero. Python provides a powerful exception handling mechanism using `try`, `except`, `else`, and `finally`.

Learning exception handling is essential for writing reliable, secure, and user-friendly software.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what exceptions are.
- Differentiate between syntax errors and runtime errors.
- Use `try` and `except` blocks.
- Handle multiple exceptions.
- Use `else` and `finally`.
- Raise custom exceptions.
- Create your own exception classes.
- Apply exception handling in real-world applications.

---

# ❓ What is an Exception?

An exception is an error that occurs while a program is running.

Examples include:

- Dividing by zero
- Opening a file that does not exist
- Entering text where a number is expected
- Accessing an invalid list index

Without exception handling, these errors usually stop the program.

---

# 🔹 Syntax Errors vs Runtime Errors

## Syntax Error

Occurs before the program starts because the code is written incorrectly.

Example:

```python
if True
    print("Hello")
```

---

## Runtime Error

Occurs while the program is running.

Example:

```python
number = 10 / 0
```

Output:

```
ZeroDivisionError
```

---

# 🛡️ The `try` and `except` Blocks

Use `try` to wrap code that may raise an exception.

Example:

```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

---

# 🔹 Handling Multiple Exceptions

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

# 🔹 The `else` Block

The `else` block runs only if no exception occurs.

Example:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"You entered {age}.")
```

---

# 🔹 The `finally` Block

The `finally` block always executes, whether an exception occurs or not.

Example:

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program finished.")
```

---

# 🔹 Raising Exceptions

You can raise exceptions manually.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

# 🔹 Custom Exceptions

You can create your own exception classes.

Example:

```python
class InvalidAgeError(Exception):
    pass

age = -2

if age < 0:
    raise InvalidAgeError("Invalid age entered.")
```

---

# 🌍 Real-World Applications

Exception handling is used in:

- Banking Systems
- Login Systems
- Online Payment Platforms
- File Processing
- APIs
- Database Applications
- Data Analysis
- Automation Scripts

---

# 💡 Best Practices

- Catch only the exceptions you expect.
- Keep `try` blocks as small as possible.
- Write meaningful error messages.
- Use `finally` to release resources.
- Avoid hiding errors with empty `except` blocks.

---

# ⚠ Common Mistakes

- Using a broad `except` unnecessarily.
- Ignoring exception messages.
- Forgetting to clean up resources.
- Catching exceptions without handling them properly.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| basic_try_except.py | Basic exception handling |
| multiple_exceptions.py | Handling multiple exceptions |
| else_finally.py | Using `else` and `finally` |
| raising_exceptions.py | Raising exceptions |
| custom_exceptions.py | Creating custom exceptions |
| file_exception.py | File handling with exceptions |
| calculator_safe.py | Calculator with error handling |

---

# 📝 Practice Exercises

1. Create a calculator that handles division by zero.
2. Ask the user for a number and handle invalid input.
3. Open a file safely and display an error if it does not exist.
4. Create a custom exception for an invalid password.
5. Build a simple login program with exception handling.

---

# 📚 Summary

Exception handling makes Python programs more reliable by preventing unexpected crashes and providing meaningful error messages. By using `try`, `except`, `else`, `finally`, and custom exceptions, you can build robust applications that handle errors gracefully.

---

## 📌 Next Chapter

➡️ **12 - Modules and Packages**
