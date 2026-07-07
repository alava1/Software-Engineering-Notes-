# student_management.py - OOP Heavy Project

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}
    
    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
            print(f"Grade added for {subject}")
        else:
            print("Grade must be between 0 and 100")
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_info(self):
        avg = self.get_average()
        return f"{self.name} (ID: {self.student_id}) - Average: {avg:.1f}"

class School:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        self.students[student.student_id] = student
    
    def show_all_students(self):
        for student in self.students.values():
            print(student.get_info())

if __name__ == "__main__":
    school = School()
    print("=== Student Management System ===\n")
    
    s1 = Student("S001", "Aisha Mohammed")
    s1.add_grade("Math", 85)
    s1.add_grade("English", 92)
    school.add_student(s1)
    
    s2 = Student("S002", "Emmanuel Okoro")
    s2.add_grade("Math", 78)
    school.add_student(s2)
    
    school.show_all_students()
