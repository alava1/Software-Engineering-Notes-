# 🔀 Chapter 05: Conditional Statements

## 📖 Introduction

Conditional statements allow a program to make decisions based on specific conditions. Instead of executing every line of code sequentially, a program can evaluate expressions and choose different paths depending on whether a condition is **True** or **False**.

Decision-making is a core programming skill used in almost every software application, from login systems to online banking and e-commerce platforms.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand Boolean logic.
- Use `if`, `elif`, and `else` statements.
- Create nested conditional statements.
- Combine multiple conditions using logical operators.
- Write decision-making programs.
- Apply conditional statements to real-world problems.

---

# 🤔 What are Conditional Statements?

Conditional statements control the flow of a program by executing different blocks of code based on whether a condition evaluates to `True` or `False`.

Example:

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

---

# ✅ The `if` Statement

The `if` statement executes code only when a condition is true.

Syntax:

```python
if condition:
    # Code to execute
```

Example:

```python
temperature = 35

if temperature > 30:
    print("It's a hot day.")
```

---

# 🔄 The `if...else` Statement

Use `else` to define what happens when the condition is false.

Example:

```python
password = "python123"

if password == "python123":
    print("Access granted.")
else:
    print("Access denied.")
```

---

# 🔀 The `if...elif...else` Statement

Use `elif` when checking multiple conditions.

Example:

```python
score = 78

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

# 🏗 Nested Conditional Statements

A nested conditional is an `if` statement inside another `if` statement.

Example:

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Identification required.")
else:
    print("You must be at least 18 years old.")
```

---

# 🔗 Combining Conditions

Logical operators make conditions more powerful.

## AND

Both conditions must be true.

```python
if age >= 18 and has_id:
    print("Access granted.")
```

## OR

Only one condition needs to be true.

```python
if is_admin or is_manager:
    print("Access granted.")
```

## NOT

Reverses a condition.

```python
if not is_logged_in:
    print("Please log in.")
```

---

# 🌍 Real-World Applications

Conditional statements are used in:

- User Authentication
- ATM Systems
- Banking Applications
- Student Result Systems
- E-commerce Websites
- Hospital Management Systems
- Online Examinations
- Inventory Systems

---

# 💡 Best Practices

- Keep conditions simple and readable.
- Avoid deeply nested `if` statements.
- Use meaningful variable names.
- Test every possible condition.
- Add comments for complex logic.

---

# ⚠ Common Mistakes

- Using `=` instead of `==`.
- Incorrect indentation.
- Forgetting the colon (`:`).
- Writing unnecessary nested conditions.
- Ignoring edge cases.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| if_statement.py | Basic `if` statement examples |
| if_else.py | `if...else` examples |
| if_elif_else.py | Multiple condition examples |
| nested_if.py | Nested conditional statements |
| logical_conditions.py | Combining conditions |
| grade_checker.py | Student grading program |
| login_system.py | Simple login verification |

---

# 📝 Practice Exercises

1. Check whether a number is positive, negative, or zero.
2. Determine whether a year is a leap year.
3. Create a simple ATM withdrawal checker.
4. Build a voting eligibility checker.
5. Create a basic login system.

---

# 📚 Summary

Conditional statements enable programs to make intelligent decisions. Mastering `if`, `elif`, and `else` is essential for building interactive applications, validating user input, and implementing business logic in real-world software.

---

## 📌 Next Chapter

➡️ **06 - Loops**
