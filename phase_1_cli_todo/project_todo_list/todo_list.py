"""
Todo List Application
A command-line application for managing tasks.

This is a starter skeleton for your project.
Complete the implementation by following the milestones in README.md
"""


def main():
    """
    Main program loop.
    
    This function contains the main loop of the application.
    It displays the menu, gets user input, and calls the appropriate functions.
    """
    print("Todo List Application")
    print("====================\n")
    
    # Initialize tasks list
    tasks = []
    
    while True:
        # Display menu
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice (1-7): ").strip()
        
        # Handle user choice
        if choice == "1":
            print("Add a task - Implement this in Milestone 2")
            # tasks = add_task(tasks)
        elif choice == "2":
            print("View all tasks - Implement this in Milestone 2")
            # view_tasks(tasks)
        elif choice == "3":
            print("Mark a task as complete - Implement this in Milestone 3")
            # tasks = mark_complete(tasks)
        elif choice == "4":
            print("Delete a task - Implement this in Milestone 3")
            # tasks = delete_task(tasks)
        elif choice == "5":
            print("Save tasks to file - Implement this in Milestone 5")
            # save_tasks(tasks)
        elif choice == "6":
            print("Load tasks from file - Implement this in Milestone 5")
            # tasks = load_tasks()
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


# TODO: Add your functions here as you complete each milestone

# Milestone 2: Task Representation
# def add_task(tasks):
#     """Add a new task to the tasks list."""
#     pass


# def view_tasks(tasks):
#     """Display all tasks in the tasks list."""
#     pass


# Milestone 3: Core Functionality
# def mark_complete(tasks):
#     """Mark a task as complete."""
#     pass


# def delete_task(tasks):
#     """Delete a task from the list."""
#     pass


# Milestone 5: File Persistence
# import json
# def save_tasks(tasks):
#     """Save tasks to a JSON file."""
#     pass


# def load_tasks():
#     """Load tasks from a JSON file."""
#     pass


# Milestone 6: Code Organization
# def get_user_choice():
#     """Get and validate user choice."""
#     pass


if __name__ == "__main__":
    main()
