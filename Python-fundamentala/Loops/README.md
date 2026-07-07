# 🔁 Chapter 06: Loops

## 📖 Introduction

Loops are one of the most powerful features in programming. They allow a program to execute a block of code repeatedly until a specified condition is met. Without loops, developers would need to write the same code multiple times, making programs longer, harder to maintain, and more prone to errors.

Python provides two main types of loops:

- **for loop** – Used when the number of iterations is known or when iterating over a collection.
- **while loop** – Used when the number of iterations is unknown and depends on a condition.

Mastering loops is essential for tasks such as processing data, automating repetitive work, and building efficient software.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the purpose of loops.
- Use `for` loops to iterate over sequences.
- Use `while` loops to repeat actions based on conditions.
- Control loop execution with `break`, `continue`, and `pass`.
- Create nested loops.
- Apply loops to solve practical programming problems.

---

# 🔄 What is a Loop?

A loop repeatedly executes a block of code until a condition becomes false or until all items in a sequence have been processed.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```
0
1
2
3
4
```

---

# 🔹 The `for` Loop

The `for` loop is commonly used to iterate through sequences such as lists, tuples, strings, and ranges.

Example:

```python
fruits = ["Apple", "Orange", "Banana"]

for fruit in fruits:
    print(fruit)
```

Output:

```
Apple
Orange
Banana
```

---

# 🔹 The `range()` Function

The `range()` function generates a sequence of numbers.

Examples:

```python
range(5)
```

Produces:

```
0 1 2 3 4
```

```python
range(1, 6)
```

Produces:

```
1 2 3 4 5
```

```python
range(2, 11, 2)
```

Produces:

```
2 4 6 8 10
```

---

# 🔹 The `while` Loop

The `while` loop continues running as long as its condition evaluates to `True`.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# 🔹 Loop Control Statements

## `break`

Stops the loop immediately.

Example:

```python
for number in range(10):
    if number == 5:
        break
    print(number)
```

---

## `continue`

Skips the current iteration and continues with the next one.

Example:

```python
for number in range(6):
    if number == 3:
        continue
    print(number)
```

---

## `pass`

Acts as a placeholder when no action is required.

Example:

```python
for number in range(5):
    if number == 2:
        pass
    print(number)
```

---

# 🔹 Nested Loops

A nested loop is a loop inside another loop.

Example:

```python
for row in range(3):
    for column in range(3):
        print(f"Row {row}, Column {column}")
```

---

# 🌍 Real-World Applications

Loops are used in:

- Reading files
- Processing databases
- Searching records
- Data analysis
- Game development
- Report generation
- Automation scripts
- Machine learning
- Cybersecurity tools

---

# 💡 Best Practices

- Avoid infinite loops.
- Use meaningful variable names.
- Keep loops simple and readable.
- Use `for` loops when iterating over collections.
- Use `while` loops when repetition depends on a condition.

---

# ⚠ Common Mistakes

- Forgetting to update the loop variable in a `while` loop.
- Creating infinite loops unintentionally.
- Using the wrong type of loop.
- Writing deeply nested loops that reduce readability.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| for_loop.py | Basic `for` loop examples |
| while_loop.py | Basic `while` loop examples |
| range_function.py | Using the `range()` function |
| break_continue.py | Loop control statements |
| nested_loops.py | Nested loop examples |
| multiplication_table.py | Multiplication table program |
| number_guessing.py | Number guessing game |

---

# 📝 Practice Exercises

1. Print numbers from 1 to 100.
2. Display all even numbers from 1 to 50.
3. Calculate the sum of numbers from 1 to 100.
4. Generate a multiplication table.
5. Count vowels in a word.
6. Reverse a string using a loop.
7. Create a simple countdown timer.

---

# 📚 Summary

Loops make programs efficient by reducing repetition and automating tasks. Understanding `for` loops, `while` loops, and loop control statements is essential for solving real-world programming problems and building scalable software.

---

## 📌 Next Chapter

➡️ **07 - Functions**
