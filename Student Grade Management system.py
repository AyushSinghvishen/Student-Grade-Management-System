# Simple Student Grade Management System
# Using Python basics, control flow, and data structures

# Sample student records
students = [
    {"id": 1, "name": "Alice", "grades": [85, 90, 78]},
    {"id": 2, "name": "Bob", "grades": [70, 75, 80]},
    {"id": 3, "name": "Charlie", "grades": [95, 88, 92]},
]

# Function to display all students
def display_students():
    print("\nStudent Records:")
    for student in students:
        avg_grade = sum(student["grades"]) / len(student["grades"])
        print(f"ID: {student['id']} | Name: {student['name']} | Grades: {student['grades']} | Average: {avg_grade:.2f}")

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    grades_input = input("Enter grades separated by spaces: ")
    grades = [int(g) for g in grades_input.split()]
    student_id = max(student["id"] for student in students) + 1 if students else 1
    students.append({"id": student_id, "name": name, "grades": grades})
    print(f"Student '{name}' added with ID {student_id}.")

# Function to calculate grade for a student
def student_average():
    display_students()
    student_id = int(input("\nEnter the student ID to calculate average grade: "))
    for student in students:
        if student["id"] == student_id:
            avg = sum(student["grades"]) / len(student["grades"])
            print(f"{student['name']}'s average grade is: {avg:.2f}")
            return
    print("Student ID not found.")

# Function to update student grades
def update_grades():
    display_students()
    student_id = int(input("\nEnter the student ID to update grades: "))
    for student in students:
        if student["id"] == student_id:
            grades_input = input("Enter new grades separated by spaces: ")
            student["grades"] = [int(g) for g in grades_input.split()]
            print(f"Grades updated for {student['name']}.")
            return
    print("Student ID not found.")

# Main program loop
while True:
    print("\nStudent Grade Management System")
    print("1. Display all students")
    print("2. Add a student")
    print("3. Calculate student average")
    print("4. Update student grades")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        student_average()
    elif choice == "4":
        update_grades()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
