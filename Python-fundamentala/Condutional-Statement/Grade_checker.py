# grade_checker.py
# Topic: if...elif...else (Multiple conditions)

print("=== Student Grade Checker ===\n")

# Get input from user
try:
    score = float(input("Enter your score (0-100): "))
    
    # Input validation
    if score < 0 or score > 100:
        print("❌ Error: Score must be between 0 and 100.")
    else:
        # Main grading logic
        if score >= 90:
            grade = "A"
            message = "Excellent! Outstanding performance!"
        elif score >= 80:
            grade = "B"
            message = "Very Good! Keep it up!"
        elif score >= 70:
            grade = "C"
            message = "Good. You passed."
        elif score >= 60:
            grade = "D"
            message = "Pass. You need to work harder."
        else:
            grade = "F"
            message = "Failed. Please study more."
        
        print(f"Your Grade: {grade}")
        print(f"Feedback: {message}")

except ValueError:
    print("❌ Invalid input! Please enter a number.")
