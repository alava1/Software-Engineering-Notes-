# ⌨️ Chapter 04: Input and Output

## 📖 Introduction

Input and Output (I/O) are fundamental concepts in programming that allow a program to communicate with users. Input enables users to provide data, while output displays information back to the user.

Almost every software application—from calculators to banking systems—relies on input and output to function effectively.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the concepts of input and output.
- Display information using the `print()` function.
- Accept user input using the `input()` function.
- Convert user input into different data types.
- Format output using different techniques.
- Build simple interactive Python programs.

---

# 📤 Output in Python

Python uses the `print()` function to display information on the screen.

Example:

```python
print("Hello, World!")
```

Output:

```
Hello, World!
```

You can also print numbers and variables:

```python
name = "Lawal"
age = 22

print(name)
print(age)
```

---

# 📥 Input in Python

Python uses the `input()` function to receive information from the user.

Example:

```python
name = input("Enter your name: ")

print("Welcome,", name)
```

---

# 🔄 Type Conversion

The `input()` function always returns a string. If you need a number, convert it.

Example:

```python
age = int(input("Enter your age: "))

print(age)
```

For decimal numbers:

```python
price = float(input("Enter price: "))
```

---

# 🎨 Formatted Output

Python provides several ways to format output.

### Using f-strings (Recommended)

```python
name = "Lawal"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

### Using `.format()`

```python
print("My name is {}.".format(name))
```

### Using commas

```python
print("Name:", name)
```

---

# 🧮 Example Program

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old.")
```

---

# 💡 Best Practices

- Write clear input prompts.
- Validate user input where possible.
- Use f-strings for readable output.
- Convert data to the correct type before calculations.
- Keep messages simple and user-friendly.

---

# ⚠ Common Mistakes

- Forgetting that `input()` returns a string.
- Performing calculations without converting input.
- Using unclear prompts.
- Printing variables before assigning values.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| print_function.py | Using the `print()` function |
| user_input.py | Reading user input |
| type_conversion.py | Converting input values |
| formatted_output.py | Displaying formatted output |
| mini_calculator.py | Simple interactive calculator |

---

# 📚 Summary

Input and Output allow programs to interact with users. By combining the `input()` and `print()` functions with proper type conversion and formatting, you can build interactive applications that respond to user actions.

---

## 📌 Next Chapter

➡️ **05 - Conditional Statements**
