# dictionaries.py
# Topic: Dictionaries - Key-Value pairs (like a real dictionary)

print("=== Dictionaries ===\n")

# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "course": "Computer Science",
    "grades": [85, 90, 78]
}

print("Student info:", student)
print("Student name:", student["name"])
print("Student age:", student.get("age"))

# Adding new key-value
student["city"] = "Abuja"
print("\nAfter adding city:", student)

# Modifying
student["age"] = 21

# Looping through dictionary
print("\nAll keys and values:")
for key, value in student.items():
    print(f"{key}: {value}")

# Check if key exists
if "grades" in student:
    print("\nAverage grade:", sum(student["grades"]) / len(student["grades"]))
