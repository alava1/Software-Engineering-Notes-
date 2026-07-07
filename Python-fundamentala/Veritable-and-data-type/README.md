# 📦 Chapter 02: Variables and Data Types

## 📖 Introduction

Variables are one of the most fundamental concepts in programming. They allow us to store, retrieve, and manipulate data while a program is running.

Every application—from a simple calculator to a banking system—uses variables to manage information such as names, numbers, prices, dates, and user input.

This chapter introduces variables, data types, type conversion, naming conventions, and best practices in Python.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what variables are.
- Declare and assign variables.
- Identify Python's built-in data types.
- Perform type conversion.
- Follow Python variable naming conventions.
- Write clean and readable code.

---

# 📝 What is a Variable?

A variable is a named storage location used to hold data in memory.

Think of a variable as a labeled container that stores information, which can be updated or reused throughout a program.

Example:

```python
name = "Lawal Yunusa"
age = 22
```

In this example:

- `name` stores text.
- `age` stores a number.

---

# 🔤 Variable Naming Rules

Python variable names:

- Must begin with a letter or underscore (`_`).
- Cannot begin with a number.
- Can contain letters, numbers, and underscores.
- Are case-sensitive.

### ✅ Valid Examples

```python
student_name = "Lawal"
age = 22
_total = 100
```

### ❌ Invalid Examples

```python
2name = "Lawal"
student-name = "Lawal"
class = "Python"
```

---

# 📚 Python Data Types

Python provides several built-in data types.

## String (`str`)

Stores text.

```python
name = "Lawal Yunusa"
```

---

## Integer (`int`)

Stores whole numbers.

```python
age = 22
```

---

## Float (`float`)

Stores decimal numbers.

```python
height = 1.75
```

---

## Boolean (`bool`)

Represents either `True` or `False`.

```python
is_student = True
```

---

## List (`list`)

Stores multiple values in order.

```python
languages = ["Python", "Java", "C++"]
```

---

## Tuple (`tuple`)

Stores ordered values that cannot be changed.

```python
coordinates = (10, 20)
```

---

## Dictionary (`dict`)

Stores data as key-value pairs.

```python
student = {
    "name": "Lawal",
    "age": 22
}
```

---

## Set (`set`)

Stores unique values.

```python
numbers = {1, 2, 3, 4}
```

---

# 🔄 Type Conversion

Python allows conversion between data types.

Examples:

```python
age = "22"

age = int(age)
```

```python
price = 250

price = float(price)
```

```python
number = 45

number = str(number)
```

---

# 🔍 Checking Data Types

Use the `type()` function.

Example:

```python
name = "Lawal"

print(type(name))
```

Output:

```
<class 'str'>
```

---

# 💡 Best Practices

- Use meaningful variable names.
- Follow the `snake_case` naming convention.
- Avoid single-letter variable names except in loops.
- Keep variable names descriptive.
- Write readable code.

---

# ⚠ Common Mistakes

- Using reserved keywords as variable names.
- Starting variable names with numbers.
- Confusing strings with numbers.
- Ignoring case sensitivity.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| variables.py | Creating and using variables |
| data_types.py | Python data types |
| type_conversion.py | Converting between data types |
| type_checking.py | Using the `type()` function |
| naming_conventions.py | Variable naming best practices |

---

# 📚 Summary

Variables are the building blocks of programming. Understanding how to store, retrieve, and manipulate data is essential for writing effective Python programs.

Mastering variables and data types prepares you for decision-making, loops, functions, and object-oriented programming.

---

## 📌 Next Chapter

➡️ **03 - Operators**
