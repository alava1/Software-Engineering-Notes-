# 📂 Chapter 10: File Handling

## 📖 Introduction

File handling is the process of creating, reading, writing, updating, and managing files on a computer. It allows programs to store information permanently so that data is available even after the program has stopped running.

Without file handling, every time a program closes, all data stored in memory is lost. By using files, applications can save user information, logs, reports, configurations, and many other types of data.

Python provides built-in functions that make working with files simple and efficient.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the purpose of file handling.
- Open and close files safely.
- Read data from text files.
- Write and append data to files.
- Use different file modes.
- Work with the `with` statement.
- Handle common file-related errors.

---

# 📁 What is File Handling?

File handling allows a program to interact with files stored on a computer.

Common operations include:

- Creating files
- Opening files
- Reading files
- Writing files
- Updating files
- Deleting files

---

# 📂 Opening a File

Use the `open()` function to open a file.

Example:

```python
file = open("example.txt", "r")
```

The first argument is the file name, while the second argument specifies the file mode.

---

# 📖 File Modes

| Mode | Description |
|------|-------------|
| `r` | Read a file |
| `w` | Write to a file (creates or overwrites) |
| `a` | Append data to a file |
| `x` | Create a new file |
| `rb` | Read a binary file |
| `wb` | Write a binary file |

---

# 📥 Reading Files

Read the entire file:

```python
file = open("example.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# ✍️ Writing to a File

Example:

```python
file = open("notes.txt", "w")

file.write("Learning Python File Handling")

file.close()
```

If the file does not exist, Python creates it.

---

# ➕ Appending to a File

Append adds new content without removing existing content.

Example:

```python
file = open("notes.txt", "a")

file.write("\nPractice every day.")

file.close()
```

---

# ✅ Using the `with` Statement

The recommended way to work with files is by using the `with` statement.

Example:

```python
with open("example.txt", "r") as file:
    content = file.read()

print(content)
```

The file is automatically closed when the block finishes.

---

# ⚠ Handling File Errors

Example:

```python
try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

# 🌍 Real-World Applications

File handling is used in:

- Student record systems
- Banking applications
- Logging systems
- Configuration files
- Report generation
- Data backup
- Inventory management
- User profile storage

---

# 💡 Best Practices

- Always close files after use.
- Prefer the `with` statement.
- Handle exceptions gracefully.
- Use meaningful file names.
- Avoid hardcoding file paths when possible.

---

# ⚠ Common Mistakes

- Forgetting to close a file.
- Using the wrong file mode.
- Overwriting important data unintentionally.
- Assuming a file always exists.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| create_file.py | Creating a new file |
| read_file.py | Reading from a file |
| write_file.py | Writing to a file |
| append_file.py | Appending data |
| file_modes.py | Demonstrating file modes |
| with_statement.py | Using the `with` statement |
| file_exceptions.py | Handling file-related errors |

---

# 📝 Practice Exercises

1. Create a file named `students.txt`.
2. Write five student names into the file.
3. Read and display the contents.
4. Append a new student name.
5. Count the number of lines in a file.
6. Build a simple notes application using text files.

---

# 📚 Summary

File handling allows Python programs to store and retrieve data permanently. By understanding file modes, reading and writing operations, and using the `with` statement, you can build applications that manage data safely and efficiently.

---

## 📌 Next Chapter

➡️ **11 - Exception Handling**
