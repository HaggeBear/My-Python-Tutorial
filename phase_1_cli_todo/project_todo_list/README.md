# Todo List Application - Project

## 🎯 Project Overview

**Congratulations on reaching the capstone project of Phase 1!**

In this project, you'll build a **Command-Line Todo List Application** that allows users to:
- Add tasks to their todo list
- View all their tasks
- Mark tasks as complete
- Delete tasks
- Save their tasks to a file
- Load their tasks from a file

This project will bring together **everything** you've learned in Phase 1:
- Variables and data types
- User input and output
- Conditionals (if/elif/else)
- Loops (for and while)
- Lists and dictionaries
- Functions
- File I/O (introduction to Phase 2 concepts)

---

## 📚 Learning Objectives

By completing this project, you will:
- Apply all concepts from Phase 1 in a real-world application
- Practice writing clean, organized code
- Learn to break down a large project into smaller, manageable pieces
- Gain experience with user input validation
- Understand the importance of code structure and organization
- Build confidence in your ability to create complete programs

---

## 🗺️ Project Roadmap

This project is divided into **7 milestones**. Complete each milestone before moving to the next.

### Milestone 1: Project Setup and Basic Structure
**Goal:** Set up the project and create the basic structure
- Create the main Python file
- Set up the main program loop
- Create a basic menu system

### Milestone 2: Task Representation
**Goal:** Decide how to represent tasks in your program
- Choose data structure for tasks (dictionary recommended)
- Each task should have: description, status (complete/incomplete)
- Create functions to add and display tasks

### Milestone 3: Core Functionality
**Goal:** Implement the basic CRUD operations
- Add tasks
- View all tasks
- Mark tasks as complete/incomplete
- Delete tasks

### Milestone 4: User Experience
**Goal:** Improve the user experience
- Add input validation
- Improve menu display
- Add helpful messages
- Handle edge cases (empty list, etc.)

### Milestone 5: File Persistence
**Goal:** Save and load tasks from a file
- Save tasks to a file (JSON format recommended)
- Load tasks from a file
- Handle file errors gracefully

### Milestone 6: Code Organization
**Goal:** Organize your code into functions
- Break down the code into logical functions
- Use function parameters and return values
- Improve code readability

### Milestone 7: Testing and Polish
**Goal:** Test your application and add final touches
- Test all functionality
- Fix any bugs
- Add any missing features
- Clean up the code

---

## 📁 Project Structure

```
project_todo_list/
├── README.md               # This file
├── todo_list.py           # Main application file
├── requirements.txt        # Dependencies (if any)
└── tests/
    └── test_todo_list.py  # Tests for your application
```

---

## 🚀 Getting Started

### Step 1: Create the Project Files

```bash
# Navigate to the project directory
cd /workspace/python_learning_journey/phase_1_cli_todo/project_todo_list

# Create the main application file
touch todo_list.py

# Create requirements file (optional for Phase 1)
touch requirements.txt
```

### Step 2: Start with Milestone 1

Open `todo_list.py` and start building your application.

---

## 🎯 Milestone 1: Project Setup and Basic Structure

**Goal:** Create the basic structure of your application with a menu system.

### Requirements

1. Create a main program loop that continues until the user chooses to exit
2. Display a menu with the following options:
   - Add a task
   - View all tasks
   - Mark a task as complete
   - Delete a task
   - Save tasks to file
   - Load tasks from file
   - Exit
3. Get user input for menu selection
4. Print a message based on the user's choice

### Example Menu

```
Todo List Application
====================

1. Add a task
2. View all tasks
3. Mark a task as complete
4. Delete a task
5. Save tasks to file
6. Load tasks from file
7. Exit

Enter your choice (1-7): 
```

### Starter Code

Here's a basic structure to get you started:

```python
"""
Todo List Application
A command-line application for managing tasks.
"""

def main():
    """Main program loop."""
    print("Todo List Application")
    print("====================\n")
    
    while True:
        # Display menu
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice (1-7): ").strip()
        
        # Handle user choice
        if choice == "1":
            print("Add a task - Coming soon!")
        elif choice == "2":
            print("View all tasks - Coming soon!")
        elif choice == "3":
            print("Mark a task as complete - Coming soon!")
        elif choice == "4":
            print("Delete a task - Coming soon!")
        elif choice == "5":
            print("Save tasks to file - Coming soon!")
        elif choice == "6":
            print("Load tasks from file - Coming soon!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


def display_menu():
    """Display the main menu."""
    print("\nTodo List Application")
    print("====================")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")
    print()


if __name__ == "__main__":
    main()
```

### Your Tasks for Milestone 1

1. [ ] Create the `todo_list.py` file
2. [ ] Copy the starter code above
3. [ ] Run the program to verify it works
4. [ ] Test the menu system
5. [ ] Make sure the exit option works

---

## 🎯 Milestone 2: Task Representation

**Goal:** Decide how to represent tasks and implement basic task operations.

### Requirements

1. Choose a data structure to store tasks (dictionary recommended)
2. Each task should have:
   - A description (string)
   - A status (complete/incomplete - boolean or string)
   - An ID (optional, for easier management)
3. Create a list to store all tasks
4. Implement the "Add a task" functionality
5. Implement the "View all tasks" functionality

### Task Representation Options

**Option 1: Dictionary for each task**
```python
tasks = [
    {"id": 1, "description": "Buy groceries", "completed": False},
    {"id": 2, "description": "Walk the dog", "completed": True},
]
```

**Option 2: Separate lists**
```python
task_descriptions = ["Buy groceries", "Walk the dog"]
task_statuses = [False, True]
```

**Recommendation:** Use Option 1 (list of dictionaries). It's more flexible and easier to work with.

### Functions to Implement

```python
def add_task(tasks):
    """
    Add a new task to the tasks list.
    
    Args:
        tasks: List of task dictionaries
        
    Returns:
        Updated list of tasks
    """
    # Get task description from user
    description = input("Enter task description: ").strip()
    
    # Create new task dictionary
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }
    
    # Add to tasks list
    tasks.append(new_task)
    print(f"Task added: {description}")
    
    return tasks


def view_tasks(tasks):
    """
    Display all tasks in the tasks list.
    
    Args:
        tasks: List of task dictionaries
    """
    if not tasks:
        print("No tasks in the list.")
        return
    
    print("\nYour Tasks:")
    print("-" * 30)
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['description']}")
    print("-" * 30)
```

### Your Tasks for Milestone 2

1. [ ] Add a `tasks` list to store tasks
2. [ ] Implement the `add_task()` function
3. [ ] Implement the `view_tasks()` function
4. [ ] Update the main loop to call these functions
5. [ ] Test adding and viewing tasks

---

## 🎯 Milestone 3: Core Functionality

**Goal:** Implement the remaining CRUD operations (Mark complete, Delete).

### Requirements

1. Implement "Mark a task as complete"
2. Implement "Delete a task"
3. Add input validation
4. Handle edge cases (empty list, invalid IDs, etc.)

### Functions to Implement

```python
def mark_complete(tasks):
    """
    Mark a task as complete.
    
    Args:
        tasks: List of task dictionaries
        
    Returns:
        Updated list of tasks
    """
    # Check if there are tasks
    if not tasks:
        print("No tasks to mark as complete.")
        return tasks
    
    # Display tasks with numbers
    view_tasks(tasks)
    
    # Get task ID from user
    try:
        task_id = int(input("Enter task ID to mark as complete: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return tasks
    
    # Find and update the task
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task {task_id} marked as complete.")
            return tasks
    
    # Task not found
    print(f"Task with ID {task_id} not found.")
    return tasks


def delete_task(tasks):
    """
    Delete a task from the list.
    
    Args:
        tasks: List of task dictionaries
        
    Returns:
        Updated list of tasks
    """
    # Check if there are tasks
    if not tasks:
        print("No tasks to delete.")
        return tasks
    
    # Display tasks with numbers
    view_tasks(tasks)
    
    # Get task ID from user
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return tasks
    
    # Find and delete the task
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(i)
            print(f"Task '{deleted_task['description']}' deleted.")
            return tasks
    
    # Task not found
    print(f"Task with ID {task_id} not found.")
    return tasks
```

### Your Tasks for Milestone 3

1. [ ] Implement the `mark_complete()` function
2. [ ] Implement the `delete_task()` function
3. [ ] Update the main loop to call these functions
4. [ ] Test all CRUD operations
5. [ ] Make sure edge cases are handled

---

## 🎯 Milestone 4: User Experience

**Goal:** Improve the user experience with validation and better messages.

### Requirements

1. Add input validation for all user inputs
2. Improve error messages
3. Add confirmation for destructive actions (delete)
4. Handle edge cases gracefully
5. Add clear feedback for all actions

### Improvements to Make

```python
# In main() - Validate menu choice
if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
    print("Invalid choice. Please enter a number between 1 and 7.")
    continue

# In delete_task() - Add confirmation
confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip().lower()
if confirm != "y":
    print("Deletion cancelled.")
    return tasks

# In add_task() - Validate description
if not description:
    print("Task description cannot be empty.")
    return tasks
```

### Your Tasks for Milestone 4

1. [ ] Add input validation for all user inputs
2. [ ] Add confirmation for delete operations
3. [ ] Improve error messages
4. [ ] Handle edge cases (empty list, invalid IDs)
5. [ ] Test the improved user experience

---

## 🎯 Milestone 5: File Persistence

**Goal:** Save and load tasks from a file.

### Requirements

1. Save tasks to a JSON file
2. Load tasks from a JSON file
3. Handle file errors gracefully
4. Add file name input or use a default

### Using JSON for File Storage

Python has a built-in `json` module that makes it easy to save and load data:

```python
import json

# Save tasks to file
def save_tasks(tasks, filename="tasks.json"):
    """
    Save tasks to a JSON file.
    
    Args:
        tasks: List of task dictionaries
        filename: Name of the file to save to
    """
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=2)
        print(f"Tasks saved to {filename}")
    except Exception as e:
        print(f"Error saving tasks: {e}")


# Load tasks from file
def load_tasks(filename="tasks.json"):
    """
    Load tasks from a JSON file.
    
    Args:
        filename: Name of the file to load from
        
    Returns:
        List of task dictionaries, or empty list if file doesn't exist
    """
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print(f"Tasks loaded from {filename}")
        return tasks
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty task list.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
```

### Your Tasks for Milestone 5

1. [ ] Import the `json` module
2. [ ] Implement the `save_tasks()` function
3. [ ] Implement the `load_tasks()` function
4. [ ] Update the main loop to call these functions
5. [ ] Test saving and loading tasks
6. [ ] Handle file errors gracefully

---

## 🎯 Milestone 6: Code Organization

**Goal:** Organize your code into well-structured functions.

### Requirements

1. Break down the code into logical functions
2. Use function parameters and return values appropriately
3. Remove duplicate code
4. Improve code readability
5. Add docstrings to all functions

### Suggested Function Structure

```python
"""
Todo List Application
A command-line application for managing tasks.
"""

import json


def main():
    """Main program loop."""
    tasks = []
    
    # Load tasks at startup
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            tasks = add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            tasks = mark_complete(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
        elif choice == "6":
            tasks = load_tasks()
        elif choice == "7":
            print("Goodbye!")
            break


def display_menu():
    """Display the main menu."""
    # ... menu display code ...


def get_user_choice():
    """
    Get and validate user choice.
    
    Returns:
        Validated user choice as string
    """
    # ... input validation code ...


# Task management functions

def add_task(tasks):
    """Add a new task."""
    # ... implementation ...


def view_tasks(tasks):
    """Display all tasks."""
    # ... implementation ...


def mark_complete(tasks):
    """Mark a task as complete."""
    # ... implementation ...


def delete_task(tasks):
    """Delete a task."""
    # ... implementation ...


# File operations

def save_tasks(tasks):
    """Save tasks to file."""
    # ... implementation ...


def load_tasks():
    """Load tasks from file."""
    # ... implementation ...


if __name__ == "__main__":
    main()
```

### Your Tasks for Milestone 6

1. [ ] Organize code into logical functions
2. [ ] Add docstrings to all functions
3. [ ] Use parameters and return values appropriately
4. [ ] Remove duplicate code
5. [ ] Improve code readability

---

## 🎯 Milestone 7: Testing and Polish

**Goal:** Test your application thoroughly and add final touches.

### Requirements

1. Test all functionality
2. Fix any bugs
3. Add any missing features
4. Clean up the code
5. Add comments where necessary

### Testing Checklist

- [ ] Add a task
- [ ] View tasks (empty list and with tasks)
- [ ] Mark a task as complete
- [ ] Mark a task as incomplete (if you added this feature)
- [ ] Delete a task (with confirmation)
- [ ] Save tasks to file
- [ ] Load tasks from file
- [ ] Exit the program
- [ ] Invalid menu choices
- [ ] Empty task description
- [ ] Invalid task IDs
- [ ] Delete confirmation cancellation
- [ ] File not found when loading

### Your Tasks for Milestone 7

1. [ ] Test all functionality listed above
2. [ ] Fix any bugs you find
3. [ ] Add any missing features
4. [ ] Clean up the code
5. [ ] Add comments where necessary
6. [ ] Run the final version and verify everything works

---

## 🎉 Final Project Checklist

Before submitting your project, make sure you can check off all of these:

### Functionality
- [ ] Users can add tasks
- [ ] Users can view all tasks
- [ ] Users can mark tasks as complete
- [ ] Users can delete tasks (with confirmation)
- [ ] Users can save tasks to a file
- [ ] Users can load tasks from a file
- [ ] Users can exit the program
- [ ] Menu system works correctly
- [ ] Input validation is implemented
- [ ] Edge cases are handled

### Code Quality
- [ ] Code is organized into functions
- [ ] Functions have docstrings
- [ ] Variable names are descriptive
- [ ] Code follows PEP 8 style guide
- [ ] No duplicate code
- [ ] Comments explain complex logic

### User Experience
- [ ] Clear menu and prompts
- [ ] Helpful error messages
- [ ] Confirmation for destructive actions
- [ ] Clear feedback for all actions
- [ ] Handles invalid input gracefully

---

## 🌟 Bonus Features (Optional)

If you want to go above and beyond, try implementing these additional features:

1. **Task Priorities:** Add priority levels to tasks (High, Medium, Low)
2. **Due Dates:** Add due dates to tasks
3. **Task Categories:** Allow categorizing tasks (Work, Personal, etc.)
4. **Search Functionality:** Search for tasks by description
5. **Sort Tasks:** Sort tasks by ID, description, status, etc.
6. **Edit Tasks:** Allow editing task descriptions
7. **Multiple Files:** Allow loading/saving from different files
8. **Color Output:** Use ANSI color codes for better display
9. **Statistics:** Show statistics (total tasks, completed tasks, etc.)
10. **Undo/Redo:** Implement undo/redo functionality

---

## 📝 Project Submission

Once you've completed your project:

1. Review the final checklist above
2. Make sure all required functionality works
3. Clean up any test code or comments
4. Save your final version of `todo_list.py`

**You've completed Phase 1!** 🎉

---

## 🚀 Next Steps

After completing this project:
1. Review what you've learned in Phase 1
2. Celebrate your accomplishment!
3. Move on to **Phase 2: Data Persistence & Organization**

---

## 📚 Resources

- [Python Documentation - json module](https://docs.python.org/3/library/json.html)
- [PEP 8 - Python Style Guide](https://peps.python.org/pep-0008/)
- [Real Python - Reading and Writing Files](https://realpython.com/read-write-files-python/)
- [Real Python - JSON in Python](https://realpython.com/python-json/)

---

**Good luck with your Todo List Application!** 🚀
