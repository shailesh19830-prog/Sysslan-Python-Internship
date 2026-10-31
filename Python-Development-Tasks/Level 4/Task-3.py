def add_task(task):
    with open("daily_tasks.txt", "a") as file:
        file.write(f"- {task}\n")
    print(f"Task added: '{task}'")

def view_tasks():
    try:
        with open("daily_tasks.txt", "r") as file:
            print("--- Your To-Do List ---")
            print(file.read())
    except FileNotFoundError:
        print("No tasks found for today.")

# Testing
add_task("Learn File Handling in Python")
add_task("Complete Internship Task")
view_tasks()