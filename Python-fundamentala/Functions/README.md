# 🧩 Chapter 07: Functions

## 📖 Introduction

Functions are reusable blocks of code designed to perform a specific task. Instead of writing the same code multiple times, you can define a function once and call it whenever needed.

Functions improve code organization, readability, reusability, and maintainability. They are a fundamental building block in Python and modern software development.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what functions are and why they are important.
- Define and call functions.
- Pass arguments to functions.
- Return values from functions.
- Use default and keyword arguments.
- Understand variable scope.
- Write reusable and modular code.

---

# 🧠 What is a Function?

A function is a named block of code that performs a specific task. Functions help reduce code duplication and make programs easier to maintain.

### Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

Output:

```
Welcome to Python!
```

---

# 📝 Defining a Function

Use the `def` keyword to define a function.

Syntax:

```python
def function_name():
    # Code block
```

Example:

```python
def welcome():
    print("Hello, World!")

welcome()
```

---

# 📥 Function Parameters

Parameters allow functions to accept input values.

Example:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Lawal")
```

Output:

```
Hello, Lawal!
```

---

# 📤 Returning Values

A function can return a result using the `return` keyword.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

Output:

```
15
```

---

# 🎯 Default Parameters

Default parameters provide a value if none is supplied.

Example:

```python
def greet(name="Guest"):
    print(f"Welcome, {name}")

greet()
greet("Lawal")
```

---

# 🔑 Keyword Arguments

Arguments can be passed by name.

Example:

```python
def student(name, age):
    print(name, age)

student(age=22, name="Lawal")
```

---

# 🌍 Variable Scope

Variables created inside a function are **local**.

Variables created outside a function are **global**.

Example:

```python
message = "Global"

def display():
    local_message = "Local"
    print(local_message)

display()
print(message)
```

---

# 🔁 Recursive Functions

A recursive function calls itself.

Example:

```python
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(5)
```

---

# 🌍 Real-World Applications

Functions are used in:

- Banking Systems
- E-commerce Platforms
- Authentication Systems
- Payment Processing
- Data Analysis
- Automation Scripts
- APIs
- Machine Learning

---

# 💡 Best Practices

- Give functions meaningful names.
- Keep each function focused on one task.
- Avoid writing very long functions.
- Add comments or docstrings where necessary.
- Return values instead of printing when appropriate.

---

# ⚠ Common Mistakes

- Forgetting to call the function.
- Using incorrect parameter names.
- Missing the `return` statement when needed.
- Making functions too complex.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| basic_functions.py | Creating and calling functions |
| parameters.py | Functions with parameters |
| return_values.py | Returning values |
| default_arguments.py | Using default parameters |
| keyword_arguments.py | Keyword arguments |
| variable_scope.py | Local and global variables |
| recursion.py | Recursive functions |
| calculator.py | Simple calculator using functions |

---

# 📝 Practice Exercises

1. Create a function to calculate the area of a rectangle.
2. Write a function that checks whether a number is even or odd.
3. Create a function to calculate a student's average score.
4. Write a recursive function to calculate a factorial.
5. Build a simple calculator using functions.

---

# 📚 Summary

Functions make programs modular, reusable, and easier to maintain. They are a core concept in software engineering and are essential for building large, organized applications. Mastering functions will prepare you for object-oriented programming, APIs, frameworks, and real-world software projects.

---

## 📌 Next Chapter

➡️ **08 - Data Structures**
