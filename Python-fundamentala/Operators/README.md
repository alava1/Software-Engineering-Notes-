# ➕ Chapter 03: Operators in Python

## 📖 Introduction

Operators are symbols used to perform operations on variables and values. They are essential in programming because they allow us to perform calculations, compare values, assign data, and make logical decisions.

Understanding operators is important because almost every Python program uses them.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand different types of operators in Python.
- Perform arithmetic calculations.
- Compare values.
- Use logical expressions.
- Assign values efficiently.
- Work with membership and identity operators.
- Apply operators in real-world programming problems.

---

# 🔢 Types of Operators in Python

Python provides several categories of operators:

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

---

# 1️⃣ Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 5 + 3 |
| - | Subtraction | 5 - 3 |
| * | Multiplication | 5 * 3 |
| / | Division | 10 / 2 |
| // | Floor Division | 10 // 3 |
| % | Modulus | 10 % 3 |
| ** | Exponent | 2 ** 3 |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 2️⃣ Comparison Operators

Comparison operators compare two values and return either **True** or **False**.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
age = 20

print(age >= 18)
```

Output:

```
True
```

---

# 3️⃣ Assignment Operators

Assignment operators assign values to variables.

Examples:

```python
x = 5

x += 2

x -= 1

x *= 3

x /= 2
```

---

# 4️⃣ Logical Operators

Logical operators combine conditions.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be true |
| or | At least one condition is true |
| not | Reverses a condition |

Example:

```python
age = 22
student = True

print(age >= 18 and student)
```

---

# 5️⃣ Identity Operators

Identity operators compare whether two variables refer to the same object.

| Operator | Meaning |
|----------|---------|
| is | Same object |
| is not | Different object |

Example:

```python
x = [1,2]
y = x

print(x is y)
```

---

# 6️⃣ Membership Operators

Membership operators check whether a value exists in a sequence.

| Operator | Meaning |
|----------|---------|
| in | Exists |
| not in | Does not exist |

Example:

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

---

# 7️⃣ Bitwise Operators

Bitwise operators work directly with binary numbers.

Examples include:

- &
- |
- ^
- ~
- <<
- >>

These are commonly used in low-level programming and optimization.

---

# 💡 Best Practices

- Use parentheses to improve readability.
- Avoid overly complex expressions.
- Use comparison operators carefully.
- Keep logical expressions simple.
- Write meaningful variable names.

---

# ⚠ Common Mistakes

- Confusing `=` with `==`.
- Dividing integers without considering float results.
- Using `is` instead of `==` for value comparison.
- Writing overly complex logical expressions.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| arithmetic.py | Arithmetic operators |
| comparison.py | Comparison operators |
| assignment.py | Assignment operators |
| logical.py | Logical operators |
| identity.py | Identity operators |
| membership.py | Membership operators |
| bitwise.py | Bitwise operators |

---

# 📚 Summary

Operators are fundamental tools that allow programs to perform calculations, compare values, make decisions, and manipulate data efficiently. A solid understanding of operators is essential before learning conditional statements, loops, and functions.

---

## 📌 Next Chapter

➡️ **04 - Input and Output**
