# Project 1: CLI Todo List

## 🎯 Goal
Learn Python fundamentals by building a command-line todo list.

---

## 📌 Start Here (10 lines)

```python
# todo.py - Your first version
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
```

Save as `project-1-todo/todo.py` and run with `python todo.py`

---

## 🚀 Next Steps (Improve Gradually)

1. **Add delete functionality**
   - Let users delete tasks by number

2. **Add complete/incomplete status**
   - Track which tasks are done

3. **Save to file**
   - Save todos to a text file
   - Load todos when starting

4. **Add due dates**
   - Let users add dates to tasks

5. **Add categories/tags**
   - Organize tasks by type

---

## 💡 Tips

- Start with the 10-line version
- Get it working first
- Then add one feature at a time
- Test after each change
- Commit to GitHub often
