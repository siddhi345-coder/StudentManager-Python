from file_handler import load_students, save_students


def add_student():
    students = load_students()

    roll = input("Enter Roll Number: ")

    # Check duplicate roll
    for student in students:
        if student["roll"] == roll:
            print("Student with this Roll Number already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")

    students.append({
        "roll": roll,
        "name": name,
        "age": age
    })

    save_students(students)
    print("Student added successfully!")
