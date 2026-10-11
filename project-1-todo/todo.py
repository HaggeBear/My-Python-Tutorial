# CLI Todo List - Starter Code
# Save this as: project-1-todo/todo.py

todos = []

def add():
    task = input("Enter task: ")
    todos.append(task)

def view():
    for i, task in enumerate(todos, 1):
        print(f"{i}. {task}")

while True:
    print("\n1. Add  2. View  3. Quit")
    choice = input("> ")
    if choice == "1": add()
    elif choice == "2": view()
    elif choice == "3": break
