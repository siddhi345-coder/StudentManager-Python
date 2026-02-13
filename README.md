# 🎓 Student Manager (Python CLI Project)

A simple command-line based Student Management System built using Python.
This project allows you to add, view, update, and delete student records with permanent data storage using a JSON file.

---

## 📌 Features

* Add new students
* View all students
* Update existing student details
* Delete student records
* Prevent duplicate roll numbers
* Persistent storage using `students.json`
* Modular file structure (separate file for each operation)

---

## 📁 Project Structure

```
student_manager/
│
├── main.py
├── file_handler.py
├── add_student.py
├── view_student.py
├── update_student.py
├── delete_student.py
└── students.json
```

---

## ⚙️ How It Works

* `main.py` → Displays menu and controls program flow
* `file_handler.py` → Handles loading and saving data
* `add_student.py` → Adds a new student
* `view_student.py` → Displays all students
* `update_student.py` → Updates student details
* `delete_student.py` → Deletes a student
* `students.json` → Stores student data permanently

All data is stored in JSON format, so it remains saved even after closing the program.

---

## ▶️ How To Run

1. Open terminal inside the project folder.
2. Run the following command:

```
python main.py
```

3. Select an option from the menu.

---

## 💾 Data Storage Format

Students are stored in `students.json` like this:

```json
[
    {
        "roll": "101",
        "name": "John",
        "age": "20"
    }
]
```

---

## 🛠 Requirements

* Python 3.x
* No external libraries required (uses built-in `json` and `os` modules)

---

## 🚀 Future Improvements

* Add search functionality
* Add validation for age input
* Convert to GUI version (Tkinter)
* Use SQLite database instead of JSON
* Add login/authentication system

---

## 👨‍💻 Author

siddhi
Python Student Manager Project

---



