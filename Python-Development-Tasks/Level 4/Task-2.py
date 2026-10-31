def generate_report(students_data):
    print(f"{'Name':<10} | {'Marks':<5} | {'Result':<5}")
    print("-" * 26)
    for name, marks in students_data.items():
        result = "Pass" if marks >= 40 else "Fail"
        print(f"{name:<10} | {marks:<5} | {result:<5}")

# Dictionary of students
students = {
    "Shailesh": 85,
    "Amit": 35,
    "Riya": 92,
    "Rahul": 38
}

generate_report(students)