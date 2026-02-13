from file_handler import load_students


def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n------ Student List ------")
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}")
    print("--------------------------")
