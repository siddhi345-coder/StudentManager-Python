from file_handler import load_students, save_students


def update_student():
    students = load_students()
    roll = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new Name: ")
            student["age"] = input("Enter new Age: ")
            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")
