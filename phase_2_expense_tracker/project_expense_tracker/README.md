# Expense Tracker Application - Project

## 🎯 Project Overview

**Welcome to the Expense Tracker project!** This is the capstone project for Phase 2, where you'll build a **Personal Expense Tracker** application.

This project will help you:
- Apply file I/O concepts in a real-world application
- Practice code organization with modules
- Work with CSV and JSON file formats
- Build a complete, functional application
- Gain experience with data persistence

---

## 📚 Learning Objectives

By completing this project, you will:
- Build a complete application with file persistence
- Practice reading and writing CSV and JSON files
- Organize your code into multiple modules
- Implement CRUD operations (Create, Read, Update, Delete)
- Handle user input and validation
- Generate reports and statistics from data

---

## 🗺️ Project Roadmap

This project is divided into **5 milestones**. Complete each milestone before moving to the next.

### Milestone 1: Project Setup and Data Models
**Goal:** Set up the project structure and define data models

### Milestone 2: File Services
**Goal:** Implement file reading/writing for CSV and JSON formats

### Milestone 3: Core Functionality
**Goal:** Implement transaction management and reporting

### Milestone 4: User Interface
**Goal:** Create the command-line interface

### Milestone 5: Testing and Polish
**Goal:** Test all functionality and add final touches

---

## 📁 Project Structure

```
project_expense_tracker/
├── README.md               # This file
├── expense_tracker.py     # Main application (command-line interface)
├── data/
│   ├── expenses.csv       # Sample CSV data
│   └── expenses.json      # Sample JSON data
├── models/
│   ├── __init__.py
│   ├── expense.py         # Expense model
│   └── category.py        # Category model
├── services/
│   ├── __init__.py
│   ├── file_service.py    # File operations (CSV, JSON)
│   └── report_service.py  # Report generation
├── utils/
│   ├── __init__.py
│   └── helpers.py         # Utility functions
└── tests/
    └── test_tracker.py     # Tests for the application
```

---

## 🚀 Getting Started

### Step 1: Create the Project Structure

```bash
# Navigate to the project directory
cd /workspace/python_learning_journey/phase_2_expense_tracker/project_expense_tracker

# Create the directory structure
mkdir -p models services utils tests data

# Create __init__.py files for packages
touch models/__init__.py services/__init__.py utils/__init__.py tests/__init__.py

# Create the main files
touch expense_tracker.py models/expense.py models/category.py

touch services/file_service.py services/report_service.py

touch utils/helpers.py tests/test_tracker.py

# Create sample data files
touch data/expenses.csv data/expenses.json
```

### Step 2: Start with Milestone 1

Open the files and start implementing based on the milestones below.

---

## 🎯 Milestone 1: Project Setup and Data Models

**Goal:** Set up the project structure and define how expenses and categories will be represented.

### Requirements

1. Create data models for expenses and categories
2. Create utility functions for common operations
3. Set up the basic project structure

### Data Models

#### Expense Model (`models/expense.py`)

An expense represents a single financial transaction. It should have:
- ID (unique identifier)
- Description (what the expense was for)
- Amount (how much was spent)
- Category (what category it belongs to)
- Date (when the transaction occurred)
- Type (income or expense)

```python
"""
Expense Model

This module defines the Expense class and related functionality.
"""

from datetime import datetime
from typing import Optional


class Expense:
    """
    Represents a single financial transaction.
    
    Attributes:
        id: Unique identifier for the expense
        description: Description of the transaction
        amount: Amount of the transaction (positive for income, negative for expense)
        category: Category the transaction belongs to
        date: Date of the transaction
        type: Type of transaction ('income' or 'expense')
    """
    
    def __init__(self, id: int, description: str, amount: float, 
                 category: str, date: Optional[datetime] = None, 
                 type: str = "expense"):
        """
        Initialize a new Expense.
        
        Args:
            id: Unique identifier
            description: Description of the transaction
            amount: Amount of the transaction
            category: Category name
            date: Date of the transaction (defaults to current date)
            type: Transaction type ('income' or 'expense')
        """
        self.id = id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()
        self.type = type
    
    def __repr__(self):
        """Return a string representation of the expense."""
        return f"Expense(id={self.id}, description='{self.description}', " \
               f"amount={self.amount}, category='{self.category}', " \
               f"date={self.date}, type='{self.type}')"
    
    def to_dict(self) -> dict:
        """Convert the expense to a dictionary."""
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d"),
            "type": self.type
        }
    
    @classmethod
    def from_dict(cls, data: dict, id: int) -> 'Expense':
        """Create an Expense from a dictionary."""
        return cls(
            id=id,
            description=data["description"],
            amount=data["amount"],
            category=data["category"],
            date=datetime.strptime(data["date"], "%Y-%m-%d"),
            type=data.get("type", "expense")
        )
```

#### Category Model (`models/category.py`)

A category represents a category for expenses (Food, Transportation, etc.).

```python
"""
Category Model

This module defines the Category class and related functionality.
"""

from typing import List, Optional


class Category:
    """
    Represents a category for expenses.
    
    Attributes:
        name: Name of the category
        description: Optional description
        budget: Optional budget amount for this category
    """
    
    def __init__(self, name: str, description: str = "", budget: Optional[float] = None):
        """
        Initialize a new Category.
        
        Args:
            name: Name of the category
            description: Description of the category
            budget: Budget amount for this category
        """
        self.name = name
        self.description = description
        self.budget = budget
    
    def __repr__(self):
        """Return a string representation of the category."""
        return f"Category(name='{self.name}', description='{self.description}', " \
               f"budget={self.budget})"
    
    def to_dict(self) -> dict:
        """Convert the category to a dictionary."""
        result = {"name": self.name, "description": self.description}
        if self.budget is not None:
            result["budget"] = self.budget
        return result
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Category':
        """Create a Category from a dictionary."""
        return cls(
            name=data["name"],
            description=data.get("description", ""),
            budget=data.get("budget")
        )
```

#### Utility Functions (`utils/helpers.py`)

```python
"""
Utility Functions

This module contains helper functions used throughout the application.
"""

from datetime import datetime
from typing import List, Any


def get_current_date() -> str:
    """Get the current date as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d")


def format_currency(amount: float) -> str:
    """Format a number as currency."""
    return f"${amount:,.2f}"


def validate_positive_number(value: str) -> float:
    """
    Validate that a string represents a positive number.
    
    Args:
        value: String to validate
        
    Returns:
        The parsed float value
        
    Raises:
        ValueError: If the value is not a positive number
    """
    try:
        num = float(value)
        if num <= 0:
            raise ValueError("Value must be positive")
        return num
    except ValueError:
        raise ValueError("Invalid number format")


def get_user_input(prompt: str, input_type: type = str, 
                   validation_func=None) -> Any:
    """
    Get validated user input.
    
    Args:
        prompt: The prompt to display
        input_type: The type to convert the input to
        validation_func: Optional validation function
        
    Returns:
        The validated user input
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty")
            
            value = input_type(user_input)
            
            if validation_func and not validation_func(value):
                raise ValueError("Input validation failed")
            
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
```

### Your Tasks for Milestone 1

1. [ ] Create the `models/expense.py` file with the Expense class
2. [ ] Create the `models/category.py` file with the Category class
3. [ ] Create the `utils/helpers.py` file with utility functions
4. [ ] Create `__init__.py` files for the models, services, and utils packages
5. [ ] Test that the classes can be instantiated
6. [ ] Test that the utility functions work correctly

---

## 🎯 Milestone 2: File Services

**Goal:** Implement file reading/writing for CSV and JSON formats.

### Requirements

1. Implement CSV file reading and writing
2. Implement JSON file reading and writing
3. Create functions to save/load expenses and categories
4. Handle file errors gracefully

### File Service (`services/file_service.py`)

```python
"""
File Service

This module handles reading and writing data to files (CSV and JSON).
"""

import csv
import json
from typing import List, Optional
from models.expense import Expense
from models.category import Category


def save_expenses_to_csv(expenses: List[Expense], filename: str = "data/expenses.csv") -> bool:
    """
    Save expenses to a CSV file.
    
    Args:
        expenses: List of Expense objects to save
        filename: Name of the CSV file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'description', 'amount', 'category', 'date', 'type'])
            
            for expense in expenses:
                writer.writerow([
                    expense.id,
                    expense.description,
                    expense.amount,
                    expense.category,
                    expense.date.strftime("%Y-%m-%d"),
                    expense.type
                ])
        return True
    except Exception as e:
        print(f"Error saving expenses to CSV: {e}")
        return False


def load_expenses_from_csv(filename: str = "data/expenses.csv") -> List[Expense]:
    """
    Load expenses from a CSV file.
    
    Args:
        filename: Name of the CSV file
        
    Returns:
        List of Expense objects
    """
    expenses = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            for i, row in enumerate(reader):
                try:
                    expense = Expense(
                        id=int(row[0]),
                        description=row[1],
                        amount=float(row[2]),
                        category=row[3],
                        type=row[5] if len(row) > 5 else "expense"
                    )
                    expenses.append(expense)
                except (IndexError, ValueError) as e:
                    print(f"Error parsing row {i+1}: {e}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty expense list.")
    except Exception as e:
        print(f"Error loading expenses from CSV: {e}")
    
    return expenses


def save_expenses_to_json(expenses: List[Expense], filename: str = "data/expenses.json") -> bool:
    """
    Save expenses to a JSON file.
    
    Args:
        expenses: List of Expense objects to save
        filename: Name of the JSON file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        data = [expense.to_dict() for expense in expenses]
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving expenses to JSON: {e}")
        return False


def load_expenses_from_json(filename: str = "data/expenses.json") -> List[Expense]:
    """
    Load expenses from a JSON file.
    
    Args:
        filename: Name of the JSON file
        
    Returns:
        List of Expense objects
    """
    expenses = []
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        
        for i, item in enumerate(data):
            try:
                expense = Expense.from_dict(item, i + 1)
                expenses.append(expense)
            except (KeyError, ValueError) as e:
                print(f"Error parsing expense {i+1}: {e}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty expense list.")
    except Exception as e:
        print(f"Error loading expenses from JSON: {e}")
    
    return expenses


def save_categories_to_json(categories: List[Category], filename: str = "data/categories.json") -> bool:
    """
    Save categories to a JSON file.
    
    Args:
        categories: List of Category objects to save
        filename: Name of the JSON file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        data = [category.to_dict() for category in categories]
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving categories to JSON: {e}")
        return False


def load_categories_from_json(filename: str = "data/categories.json") -> List[Category]:
    """
    Load categories from a JSON file.
    
    Args:
        filename: Name of the JSON file
        
    Returns:
        List of Category objects
    """
    categories = []
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        
        for item in data:
            try:
                category = Category.from_dict(item)
                categories.append(category)
            except (KeyError, ValueError) as e:
                print(f"Error parsing category: {e}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with default categories.")
        # Return default categories
        categories = [
            Category("Food", "Groceries, restaurants, etc."),
            Category("Transportation", "Gas, public transport, etc."),
            Category("Housing", "Rent, mortgage, utilities, etc."),
            Category("Entertainment", "Movies, concerts, hobbies, etc."),
            Category("Savings", "Savings and investments"),
            Category("Other", "Other expenses")
        ]
    except Exception as e:
        print(f"Error loading categories from JSON: {e}")
    
    return categories
```

### Sample Data Files

Create sample CSV and JSON files for testing:

**data/expenses.csv:**
```csv
id,description,amount,category,date,type
1,Grocery shopping,150.50,Food,2024-01-15,expense
2,Gas for car,50.00,Transportation,2024-01-16,expense
3,Salary,3000.00,Income,2024-01-01,income
4,Restaurant dinner,75.25,Food,2024-01-17,expense
```

**data/expenses.json:**
```json
[
  {
    "id": 1,
    "description": "Grocery shopping",
    "amount": 150.50,
    "category": "Food",
    "date": "2024-01-15",
    "type": "expense"
  },
  {
    "id": 2,
    "description": "Gas for car",
    "amount": 50.00,
    "category": "Transportation",
    "date": "2024-01-16",
    "type": "expense"
  },
  {
    "id": 3,
    "description": "Salary",
    "amount": 3000.00,
    "category": "Income",
    "date": "2024-01-01",
    "type": "income"
  }
]
```

### Your Tasks for Milestone 2

1. [ ] Implement the `save_expenses_to_csv()` function
2. [ ] Implement the `load_expenses_from_csv()` function
3. [ ] Implement the `save_expenses_to_json()` function
4. [ ] Implement the `load_expenses_from_json()` function
5. [ ] Implement the `save_categories_to_json()` function
6. [ ] Implement the `load_categories_from_json()` function
7. [ ] Create sample CSV and JSON files
8. [ ] Test all file operations

---

## 🎯 Milestone 3: Core Functionality

**Goal:** Implement transaction management and reporting functionality.

### Requirements

1. Implement CRUD operations for expenses
2. Implement category management
3. Implement summary statistics and reporting

### Report Service (`services/report_service.py`)

```python
"""
Report Service

This module provides reporting and statistics functionality.
"""

from typing import List, Dict
from datetime import datetime
from models.expense import Expense


def get_summary_statistics(expenses: List[Expense]) -> Dict[str, float]:
    """
    Calculate summary statistics for expenses.
    
    Args:
        expenses: List of Expense objects
        
    Returns:
        Dictionary with summary statistics
    """
    total_income = 0.0
    total_expenses = 0.0
    balance = 0.0
    
    for expense in expenses:
        if expense.type == "income":
            total_income += expense.amount
            balance += expense.amount
        else:
            total_expenses += expense.amount
            balance -= expense.amount
    
    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance
    }


def get_expenses_by_category(expenses: List[Expense]) -> Dict[str, List[Expense]]:
    """
    Group expenses by category.
    
    Args:
        expenses: List of Expense objects
        
    Returns:
        Dictionary with category names as keys and lists of expenses as values
    """
    categories = {}
    
    for expense in expenses:
        if expense.category not in categories:
            categories[expense.category] = []
        categories[expense.category].append(expense)
    
    return categories


def get_category_totals(expenses: List[Expense]) -> Dict[str, float]:
    """
    Calculate total amount for each category.
    
    Args:
        expenses: List of Expense objects
        
    Returns:
        Dictionary with category names as keys and total amounts as values
    """
    category_totals = {}
    
    for expense in expenses:
        if expense.category not in category_totals:
            category_totals[expense.category] = 0.0
        
        if expense.type == "expense":
            category_totals[expense.category] += expense.amount
        else:  # income
            category_totals[expense.category] -= expense.amount
    
    return category_totals


def get_expenses_by_month(expenses: List[Expense]) -> Dict[str, List[Expense]]:
    """
    Group expenses by month.
    
    Args:
        expenses: List of Expense objects
        
    Returns:
        Dictionary with month names as keys (YYYY-MM) and lists of expenses as values
    """
    monthly_expenses = {}
    
    for expense in expenses:
        month_key = expense.date.strftime("%Y-%m")
        if month_key not in monthly_expenses:
            monthly_expenses[month_key] = []
        monthly_expenses[month_key].append(expense)
    
    return monthly_expenses


def get_monthly_totals(expenses: List[Expense]) -> Dict[str, Dict[str, float]]:
    """
    Calculate monthly totals for income, expenses, and balance.
    
    Args:
        expenses: List of Expense objects
        
    Returns:
        Dictionary with month keys and nested dictionaries with totals
    """
    monthly_totals = {}
    
    for expense in expenses:
        month_key = expense.date.strftime("%Y-%m")
        
        if month_key not in monthly_totals:
            monthly_totals[month_key] = {
                "income": 0.0,
                "expenses": 0.0,
                "balance": 0.0
            }
        
        if expense.type == "income":
            monthly_totals[month_key]["income"] += expense.amount
            monthly_totals[month_key]["balance"] += expense.amount
        else:
            monthly_totals[month_key]["expenses"] += expense.amount
            monthly_totals[month_key]["balance"] -= expense.amount
    
    return monthly_totals
```

### Your Tasks for Milestone 3

1. [ ] Implement the `get_summary_statistics()` function
2. [ ] Implement the `get_expenses_by_category()` function
3. [ ] Implement the `get_category_totals()` function
4. [ ] Implement the `get_expenses_by_month()` function
5. [ ] Implement the `get_monthly_totals()` function
6. [ ] Test all reporting functions

---

## 🎯 Milestone 4: User Interface

**Goal:** Create the command-line interface for the Expense Tracker.

### Requirements

1. Create a menu system
2. Implement user interaction
3. Display formatted output
4. Handle user input validation

### Main Application (`expense_tracker.py`)

```python
"""
Expense Tracker Application

A command-line application for tracking personal expenses.
"""

from typing import List
from models.expense import Expense
from models.category import Category
from services.file_service import (
    save_expenses_to_csv, load_expenses_from_csv,
    save_expenses_to_json, load_expenses_from_json,
    save_categories_to_json, load_categories_from_json
)
from services.report_service import (
    get_summary_statistics, get_expenses_by_category,
    get_category_totals, get_monthly_totals
)
from utils.helpers import (
    format_currency, get_user_input, validate_positive_number
)


def main():
    """Main program loop."""
    print("Expense Tracker Application")
    print("==========================\n")
    
    # Load data
    expenses = load_expenses_from_json()
    categories = load_categories_from_json()
    
    # Set default categories if none loaded
    if not categories:
        categories = [
            Category("Food", "Groceries, restaurants, etc."),
            Category("Transportation", "Gas, public transport, etc."),
            Category("Housing", "Rent, mortgage, utilities, etc."),
            Category("Entertainment", "Movies, concerts, hobbies, etc."),
            Category("Savings", "Savings and investments"),
            Category("Other", "Other expenses")
        ]
    
    # Main loop
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            expenses = add_expense(expenses, categories)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            view_summary(expenses)
        elif choice == "5":
            view_monthly_report(expenses)
        elif choice == "6":
            expenses = edit_expense(expenses)
        elif choice == "7":
            expenses = delete_expense(expenses)
        elif choice == "8":
            manage_categories(categories)
        elif choice == "9":
            save_expenses_to_json(expenses)
            save_expenses_to_csv(expenses)
            save_categories_to_json(categories)
            print("Data saved successfully!")
        elif choice == "10":
            expenses = load_expenses_from_json()
            print("Data loaded successfully!")
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def display_menu():
    """Display the main menu."""
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View by Category")
    print("4. View Summary Statistics")
    print("5. View Monthly Report")
    print("6. Edit Expense")
    print("7. Delete Expense")
    print("8. Manage Categories")
    print("9. Save Data")
    print("10. Load Data")
    print("11. Exit")


def get_user_choice() -> str:
    """Get and validate user choice."""
    return get_user_input("Enter your choice (1-11): ", str)


def add_expense(expenses: List[Expense], categories: List[Category]) -> List[Expense]:
    """Add a new expense."""
    print("\n--- Add Expense ---")
    
    # Display categories
    print("Available Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.name}")
    
    # Get category choice
    cat_choice = get_user_input("Select category number: ", int)
    while cat_choice < 1 or cat_choice > len(categories):
        print("Invalid category. Please try again.")
        cat_choice = get_user_input("Select category number: ", int)
    
    selected_category = categories[cat_choice - 1].name
    
    # Get transaction type
    trans_type = get_user_input("Type (income/expense): ", str).lower()
    while trans_type not in ["income", "expense"]:
        print("Please enter 'income' or 'expense'.")
        trans_type = get_user_input("Type (income/expense): ", str).lower()
    
    # Get description
    description = get_user_input("Description: ", str)
    
    # Get amount
    amount = get_user_input("Amount: ", float, validate_positive_number)
    
    # Create new expense
    new_id = len(expenses) + 1
    new_expense = Expense(
        id=new_id,
        description=description,
        amount=amount,
        category=selected_category,
        type=trans_type
    )
    
    expenses.append(new_expense)
    print(f"Expense added: {new_expense.description} - {format_currency(new_expense.amount)}")
    
    return expenses


def view_all_expenses(expenses: List[Expense]):
    """Display all expenses."""
    print("\n--- All Expenses ---")
    
    if not expenses:
        print("No expenses found.")
        return
    
    # Sort by date
    sorted_expenses = sorted(expenses, key=lambda x: x.date, reverse=True)
    
    for expense in sorted_expenses:
        print(f"ID: {expense.id}")
        print(f"  Date: {expense.date.strftime('%Y-%m-%d')}")
        print(f"  Type: {expense.type.capitalize()}")
        print(f"  Category: {expense.category}")
        print(f"  Description: {expense.description}")
        print(f"  Amount: {format_currency(expense.amount)}")
        print()


def view_by_category(expenses: List[Expense]):
    """Display expenses grouped by category."""
    print("\n--- Expenses by Category ---")
    
    from services.report_service import get_expenses_by_category
    
    categories = get_expenses_by_category(expenses)
    
    if not categories:
        print("No expenses found.")
        return
    
    for category, exp_list in categories.items():
        print(f"\n{category}:")
        for expense in exp_list:
            print(f"  {expense.date.strftime('%Y-%m-%d')}: {expense.description} - {format_currency(expense.amount)}")


def view_summary(expenses: List[Expense]):
    """Display summary statistics."""
    print("\n--- Summary Statistics ---")
    
    stats = get_summary_statistics(expenses)
    
    print(f"Total Income: {format_currency(stats['total_income'])}")
    print(f"Total Expenses: {format_currency(stats['total_expenses'])}")
    print(f"Balance: {format_currency(stats['balance'])}")


def view_monthly_report(expenses: List[Expense]):
    """Display monthly report."""
    print("\n--- Monthly Report ---")
    
    monthly_totals = get_monthly_totals(expenses)
    
    if not monthly_totals:
        print("No expenses found.")
        return
    
    for month, totals in sorted(monthly_totals.items()):
        print(f"\n{month}:")
        print(f"  Income: {format_currency(totals['income'])}")
        print(f"  Expenses: {format_currency(totals['expenses'])}")
        print(f"  Balance: {format_currency(totals['balance'])}")


def edit_expense(expenses: List[Expense]) -> List[Expense]:
    """Edit an existing expense."""
    print("\n--- Edit Expense ---")
    
    view_all_expenses(expenses)
    
    if not expenses:
        return expenses
    
    expense_id = get_user_input("Enter expense ID to edit: ", int)
    
    # Find expense
    for expense in expenses:
        if expense.id == expense_id:
            # Get new values
            description = get_user_input("New description (leave blank to keep current): ", str)
            if description:
                expense.description = description
            
            amount = get_user_input("New amount (leave blank to keep current): ", str)
            if amount:
                expense.amount = float(amount)
            
            category = get_user_input("New category (leave blank to keep current): ", str)
            if category:
                expense.category = category
            
            print(f"Expense {expense_id} updated.")
            return expenses
    
    print(f"Expense with ID {expense_id} not found.")
    return expenses


def delete_expense(expenses: List[Expense]) -> List[Expense]:
    """Delete an expense."""
    print("\n--- Delete Expense ---")
    
    view_all_expenses(expenses)
    
    if not expenses:
        return expenses
    
    expense_id = get_user_input("Enter expense ID to delete: ", int)
    
    # Confirm deletion
    confirm = get_user_input("Are you sure? (y/n): ", str).lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return expenses
    
    # Find and delete expense
    for i, expense in enumerate(expenses):
        if expense.id == expense_id:
            expenses.pop(i)
            print(f"Expense {expense_id} deleted.")
            return expenses
    
    print(f"Expense with ID {expense_id} not found.")
    return expenses


def manage_categories(categories: List[Category]):
    """Manage expense categories."""
    print("\n--- Manage Categories ---")
    
    while True:
        print("\nCategory Options:")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Delete Category")
        print("4. Back")
        
        choice = get_user_input("Enter your choice: ", str)
        
        if choice == "1":
            view_categories(categories)
        elif choice == "2":
            categories = add_category(categories)
        elif choice == "3":
            categories = delete_category(categories)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def view_categories(categories: List[Category]):
    """Display all categories."""
    print("\n--- Categories ---")
    
    if not categories:
        print("No categories found.")
        return
    
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.name}")
        if category.description:
            print(f"   Description: {category.description}")
        if category.budget:
            print(f"   Budget: {format_currency(category.budget)}")


def add_category(categories: List[Category]) -> List[Category]:
    """Add a new category."""
    print("\n--- Add Category ---")
    
    name = get_user_input("Category name: ", str)
    description = get_user_input("Description (optional): ", str)
    budget = get_user_input("Budget (optional, leave blank for none): ", str)
    
    budget_value = None
    if budget:
        try:
            budget_value = float(budget)
        except ValueError:
            print("Invalid budget amount. Category created without budget.")
    
    new_category = Category(name, description, budget_value)
    categories.append(new_category)
    print(f"Category '{name}' added.")
    
    return categories


def delete_category(categories: List[Category]) -> List[Category]:
    """Delete a category."""
    print("\n--- Delete Category ---")
    
    view_categories(categories)
    
    if not categories:
        return categories
    
    cat_num = get_user_input("Enter category number to delete: ", int)
    
    if cat_num < 1 or cat_num > len(categories):
        print("Invalid category number.")
        return categories
    
    # Confirm deletion
    confirm = get_user_input("Are you sure? (y/n): ", str).lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return categories
    
    categories.pop(cat_num - 1)
    print("Category deleted.")
    
    return categories


if __name__ == "__main__":
    main()
```

### Your Tasks for Milestone 4

1. [ ] Create the main application file (`expense_tracker.py`)
2. [ ] Implement the menu system
3. [ ] Implement all user interaction functions
4. [ ] Connect all the services (file, report) to the UI
5. [ ] Test the complete application

---

## 🎯 Milestone 5: Testing and Polish

**Goal:** Test all functionality and add final touches.

### Requirements

1. Test all functionality thoroughly
2. Fix any bugs
3. Add error handling where missing
4. Improve user experience
5. Clean up the code

### Testing Checklist

- [ ] Add an expense
- [ ] View all expenses
- [ ] View expenses by category
- [ ] View summary statistics
- [ ] View monthly report
- [ ] Edit an expense
- [ ] Delete an expense
- [ ] Manage categories (view, add, delete)
- [ ] Save data to files (CSV and JSON)
- [ ] Load data from files (CSV and JSON)
- [ ] Handle invalid input gracefully
- [ ] Handle missing files gracefully
- [ ] Test with various edge cases

### Code Quality Checklist

- [ ] Code is organized into appropriate modules
- [ ] Functions have docstrings
- [ ] Variable names are descriptive
- [ ] Code follows PEP 8 style guide
- [ ] No duplicate code
- [ ] Comments explain complex logic
- [ ] Error handling is comprehensive

### User Experience Checklist

- [ ] Menu system is clear and intuitive
- [ ] User prompts are clear
- [ ] Error messages are helpful
- [ ] Confirmation for destructive actions
- [ ] Feedback for all actions
- [ ] Formatted output is easy to read

### Your Tasks for Milestone 5

1. [ ] Test all functionality listed above
2. [ ] Fix any bugs you find
3. [ ] Add error handling where missing
4. [ ] Improve user experience
5. [ ] Clean up the code
6. [ ] Run the final version and verify everything works

---

## 🎉 Final Project Checklist

Before submitting your project, make sure you can check off all of these:

### Functionality
- [ ] Users can add expenses/income
- [ ] Users can view all transactions
- [ ] Users can view transactions by category
- [ ] Users can view summary statistics
- [ ] Users can view monthly reports
- [ ] Users can edit transactions
- [ ] Users can delete transactions
- [ ] Users can manage categories
- [ ] Users can save data to CSV and JSON files
- [ ] Users can load data from CSV and JSON files
- [ ] Menu system works correctly
- [ ] Input validation is implemented
- [ ] Edge cases are handled

### Code Quality
- [ ] Code is organized into modules (models, services, utils)
- [ ] Functions have docstrings
- [ ] Variable names are descriptive
- [ ] Code follows PEP 8 style guide
- [ ] No duplicate code
- [ ] Comments explain complex logic
- [ ] Error handling is comprehensive

### User Experience
- [ ] Clear menu and prompts
- [ ] Helpful error messages
- [ ] Confirmation for destructive actions
- [ ] Clear feedback for all actions
- [ ] Handles invalid input gracefully
- [ ] Formatted output is readable

---

## 🌟 Bonus Features (Optional)

If you want to go above and beyond, try implementing these additional features:

1. **Search Functionality:** Search for expenses by description, category, or date range
2. **Filtering:** Filter expenses by date range, category, or amount
3. **Charts:** Generate simple text-based charts for visualizing spending
4. **Recurring Expenses:** Support for recurring expenses (monthly, weekly, etc.)
5. **Budget Tracking:** Track spending against budget for each category
6. **Multiple Users:** Support for multiple user profiles
7. **Data Export:** Export data to different formats (Excel, PDF, etc.)
8. **Data Import:** Import data from bank statement CSV files
9. **Password Protection:** Add password protection for sensitive data
10. **GUI Interface:** Create a simple GUI using Tkinter (Phase 4 concept)

---

## 📝 Project Submission

Once you've completed your project:

1. Review the final checklist above
2. Make sure all required functionality works
3. Clean up any test code or comments
4. Save your final versions of all files

**You've completed Phase 2!** 🎉

---

## 🚀 Next Steps

After completing this project:
1. Review what you've learned in Phase 2
2. Celebrate your accomplishment!
3. Move on to **Phase 3: Entering the Web (Python + HTML/CSS)**

---

## 📚 Resources

- [Python Documentation - File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Documentation - csv module](https://docs.python.org/3/library/csv.html)
- [Python Documentation - json module](https://docs.python.org/3/library/json.html)
- [PEP 8 - Python Style Guide](https://peps.python.org/pep-0008/)
- [Real Python - File Handling](https://realpython.com/read-write-files-python/)
- [Real Python - JSON in Python](https://realpython.com/python-json/)

---

**Good luck with your Expense Tracker Application!** 🚀
