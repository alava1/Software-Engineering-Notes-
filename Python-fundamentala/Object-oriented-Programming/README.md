# 🏛️ Chapter 09: Object-Oriented Programming (OOP)

## 📖 Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around **objects** rather than functions. An object combines **data (attributes)** and **behavior (methods)** into a single unit.

OOP helps developers create software that is modular, reusable, scalable, and easier to maintain. It is widely used in desktop applications, web development, mobile apps, enterprise systems, and game development.

Python fully supports Object-Oriented Programming, making it an essential skill for every software engineer.

---

# 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the principles of Object-Oriented Programming.
- Create classes and objects.
- Use constructors.
- Define attributes and methods.
- Apply the four pillars of OOP.
- Build reusable and maintainable code.

---

# 🧱 What is a Class?

A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that its objects will have.

Example:

```python
class Student:
    pass
```

---

# 🎯 What is an Object?

An object is an instance of a class.

Example:

```python
student1 = Student()
student2 = Student()
```

Each object has its own identity and data.

---

# 🏗 Constructors (`__init__`)

A constructor initializes an object when it is created.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Lawal", 22)
```

---

# 📌 Attributes

Attributes store information about an object.

Example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

---

# ⚙ Methods

Methods define what an object can do.

Example:

```python
class Car:
    def start(self):
        print("Car started.")
```

---

# 🏛 The Four Pillars of OOP

## 1. Encapsulation

Encapsulation protects an object's internal data by controlling access through methods.

Benefits:

- Data security
- Better organization
- Easier maintenance

---

## 2. Abstraction

Abstraction hides unnecessary implementation details and exposes only the essential features.

Example:

A user drives a car without needing to understand how the engine works internally.

Benefits:

- Simpler code
- Reduced complexity
- Better maintainability

---

## 3. Inheritance

Inheritance allows one class to inherit attributes and methods from another class.

Example:

```python
class Person:
    pass

class Student(Person):
    pass
```

Benefits:

- Code reuse
- Reduced duplication
- Easier maintenance

---

## 4. Polymorphism

Polymorphism allows different classes to define methods with the same name but different behaviors.

Example:

```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")
```

Benefits:

- Flexibility
- Extensibility
- Cleaner code

---

# 🌍 Real-World Applications

Object-Oriented Programming is used in:

- Banking Systems
- Hospital Management Systems
- School Management Systems
- E-commerce Platforms
- Inventory Systems
- Mobile Applications
- Desktop Applications
- APIs and Backend Services
- Game Development

---

# 💡 Best Practices

- Give classes meaningful names.
- Keep classes focused on one responsibility.
- Prefer composition when appropriate.
- Write reusable methods.
- Document classes and methods using docstrings.

---

# ⚠ Common Mistakes

- Creating overly large classes.
- Ignoring encapsulation.
- Misusing inheritance.
- Repeating code instead of reusing it.
- Giving methods too many responsibilities.

---

# 📂 Files in this Chapter

| File | Description |
|------|-------------|
| classes_and_objects.py | Creating classes and objects |
| constructors.py | Using `__init__()` |
| attributes_and_methods.py | Working with attributes and methods |
| encapsulation.py | Encapsulation examples |
| inheritance.py | Inheritance examples |
| polymorphism.py | Polymorphism examples |
| abstraction.py | Abstraction examples |
| student_management.py | Mini OOP project |

---

# 📝 Practice Exercises

1. Create a `Student` class with attributes for name, age, and department.
2. Build a `BankAccount` class with deposit and withdrawal methods.
3. Create an `Employee` class and extend it with a `Manager` class using inheritance.
4. Implement polymorphism with different animal classes.
5. Design a simple library management system using OOP principles.

---

# 📚 Summary

Object-Oriented Programming is one of the most widely used programming paradigms in software engineering. By organizing software into classes and objects and applying encapsulation, abstraction, inheritance, and polymorphism, developers can build applications that are modular, reusable, scalable, and easier to maintain.

Mastering OOP is a key step toward building professional desktop, web, and enterprise applications.

---

## 📌 Next Chapter

➡️ **10 - File Handling**
