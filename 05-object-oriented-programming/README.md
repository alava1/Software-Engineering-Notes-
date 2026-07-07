# Object-Oriented Programming (OOP)

## Overview

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around objects rather than functions. An object represents a real-world entity and combines data (attributes) with the operations (methods) that can be performed on that data.

OOP helps developers build software that is modular, reusable, maintainable, and easier to understand.

---

# Why OOP?

Object-Oriented Programming provides several advantages:

- Promotes code reusability.
- Makes software easier to maintain.
- Improves code organization.
- Simplifies debugging.
- Supports teamwork through modular design.
- Makes applications easier to extend with new features.

---

# Core Concepts of OOP

## Class

A class is a blueprint or template for creating objects.

Example:

A **Student** class may contain:

- Student ID
- Name
- Email
- Methods to register, update information, or view results

---

## Object

An object is an instance of a class.

Example:

Class:

Student

Objects:

- Lawal Yunusa
- Amina Ibrahim
- John David

Each object has its own data but follows the same structure defined by the class.

---

## Attributes

Attributes are the properties or characteristics of an object.

Example:

Student

- Name
- Age
- Department
- Registration Number

---

## Methods

Methods are functions that belong to a class.

Example:

Student

- register()
- login()
- updateProfile()
- viewResults()

---

# The Four Pillars of OOP

## 1. Encapsulation

Encapsulation means combining data and methods into a single unit while protecting internal data from unauthorized access.

### Benefits

- Data security
- Better organization
- Easier maintenance

Example:

A bank account should not allow anyone to directly change the account balance. Instead, methods such as `deposit()` and `withdraw()` control how the balance changes.

---

## 2. Abstraction

Abstraction hides unnecessary implementation details and exposes only essential functionality.

Example:

When driving a car, the driver uses the steering wheel, accelerator, and brake pedals without needing to understand how the engine works internally.

Benefits:

- Simpler code
- Reduced complexity
- Better maintainability

---

## 3. Inheritance

Inheritance allows one class to inherit properties and methods from another class.

Example:

Person

↓

Student

↓

GraduateStudent

The child class automatically gains the features of its parent class while adding its own unique functionality.

Benefits:

- Code reuse
- Reduced duplication
- Easier maintenance

---

## 4. Polymorphism

Polymorphism allows the same method to behave differently depending on the object using it.

Example:

Animal

Method:

makeSound()

Different implementations:

Dog → Bark

Cat → Meow

Cow → Moo

Benefits:

- Flexible software
- Easier extension
- Cleaner code

---

# Relationships Between Classes

## Association

Two classes work together but remain independent.

Example:

Teacher teaches Student.

---

## Aggregation

One object contains another, but both can exist independently.

Example:

Department contains Students.

If the department is deleted, students still exist.

---

## Composition

One object owns another completely.

Example:

House contains Rooms.

If the house is destroyed, its rooms no longer exist.

---

# Advantages of OOP

- Reusable code
- Easier debugging
- Better software organization
- Simplified maintenance
- Improved scalability
- Better teamwork
- Increased productivity

---

# Real-World Applications

Object-Oriented Programming is widely used in:

- Banking Systems
- Hospital Management Systems
- Library Management Systems
- E-commerce Platforms
- School Management Systems
- Mobile Applications
- Desktop Applications
- Game Development

---

# Best Practices

- Keep classes focused on one responsibility.
- Use meaningful class and method names.
- Avoid duplicate code.
- Favor composition where appropriate.
- Write clean and readable code.
- Document important classes and methods.

---

# Summary

Object-Oriented Programming is one of the most widely used programming paradigms in modern software development. By organizing software into classes and objects and applying the principles of encapsulation, abstraction, inheritance, and polymorphism, developers can build applications that are modular, reusable, scalable, and easier to maintain.
