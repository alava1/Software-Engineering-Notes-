# 📚 Chapter 08: Data Structures

## 📖 Introduction

Data structures are specialized ways of organizing, storing, and managing data so it can be accessed and modified efficiently. Choosing the right data structure improves the performance, readability, and maintainability of software.

Python provides several built-in data structures that are easy to use and powerful enough for developing everything from small scripts to enterprise applications.

This chapter introduces Python's most commonly used data structures and demonstrates how to use them effectively.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the purpose of data structures.
- Create and manipulate lists.
- Work with tuples.
- Use sets to store unique values.
- Store and retrieve data using dictionaries.
- Choose the appropriate data structure for different problems.

---

# 📦 What is a Data Structure?

A data structure is a method of organizing and storing data so that it can be used efficiently.

Good data structures help developers:

- Store information efficiently.
- Search data quickly.
- Reduce memory usage.
- Improve application performance.
- Write clean and maintainable code.

---

# 📋 Lists

A list is an ordered and mutable collection of items.

Example:

```python
languages = ["Python", "Java", "C++"]

print(languages)
```

Common list operations:

- Add items
- Remove items
- Update items
- Sort items
- Iterate through items

Useful methods:

- append()
- insert()
- remove()
- pop()
- sort()
- reverse()

---

# 📌 Tuples

A tuple is an ordered but immutable collection.

Example:

```python
coordinates = (10, 20)

print(coordinates)
```

Use tuples when data should not change.

Examples:

- GPS coordinates
- RGB colors
- Calendar dates

---

# 🎯 Sets

A set is an unordered collection of unique values.

Example:

```python
numbers = {1, 2, 3, 4, 4, 5}

print(numbers)
```

Output:

```
{1, 2, 3, 4, 5}
```

Sets automatically remove duplicates.

Useful methods:

- add()
- remove()
- discard()
- union()
- intersection()

---

# 📖 Dictionaries

A dictionary stores data as key-value pairs.

Example:

```python
student = {
    "name": "Lawal",
    "age": 22,
    "department": "Computer Science"
}

print(student["name"])
```

Common dictionary methods:

- keys()
- values()
- items()
- get()
- update()
- pop()

---

# 🔄 Nested Data Structures

Python allows combining multiple data structures.

Example:

```python
students = [
    {
        "name": "Lawal",
        "age": 22
    },
    {
        "name": "Amina",
        "age": 21
    }
]
```

Nested structures are commonly used in APIs, databases, and JSON data.

---

# 🌍 Real-World Applications

Data structures are used in:

- Banking Systems
- E-commerce Platforms
- Hospital Management Systems
- School Management Systems
- Inventory Systems
- Mobile Applications
- Web Applications
- Artificial Intelligence
- Data Science

---

# 💡 Best Practices

- Choose the right data structure.
- Use descriptive variable names.
- Avoid unnecessary nesting.
- Keep data organized.
- Understand mutable vs immutable objects.

---

# ⚠ Common Mistakes

- Confusing lists and tuples.
- Using duplicate values in sets.
- Accessing dictionary keys that do not exist.
- Modifying immutable objects.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| lists.py | Working with lists |
| tuples.py | Using tuples |
| sets.py | Working with sets |
| dictionaries.py | Dictionary operations |
| nested_structures.py | Nested data structures |
| list_methods.py | Common list methods |
| dictionary_methods.py | Common dictionary methods |

---

# 📝 Practice Exercises

1. Create a shopping list using a list.
2. Store student information in a dictionary.
3. Remove duplicate numbers using a set.
4. Create a contact list using dictionaries.
5. Build a simple inventory using nested data structures.

---

# 📚 Summary

Data structures are essential tools for organizing and managing information in Python. Lists, tuples, sets, and dictionaries each serve different purposes and are widely used in professional software development. Mastering these structures will help you write efficient, scalable, and maintainable programs.

---

## 📌 Next Chapter

➡️ **09 - Object-Oriented Programming**
