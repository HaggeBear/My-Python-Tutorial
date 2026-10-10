# Phase 2: Data Persistence & Organization 💾

## 🎯 Phase Overview

**Welcome to Phase 2!** Now that you've mastered the fundamentals of Python, it's time to learn how to **persist data** (save it to files) and **organize your code** more effectively.

In this phase, you'll build a **Personal Expense Tracker** that:
- Tracks income and expenses
- Categorizes transactions
- Saves data to files (CSV and JSON formats)
- Provides summary statistics
- Organizes code into multiple modules

---

## 📚 Learning Goals

By the end of this phase, you will be able to:

- ✅ Read from and write to text files
- ✅ Work with CSV files for tabular data
- ✅ Work with JSON files for structured data
- ✅ Handle file-related errors gracefully
- ✅ Use context managers (`with` statement) for file operations
- ✅ Organize code into multiple modules
- ✅ Import and use code from different files
- ✅ Create reusable utility functions
- ✅ Write code that follows the DRY (Don't Repeat Yourself) principle

---

## 🗺️ Phase Roadmap

### Week 1: File Operations
- **Day 1:** Reading and writing text files
- **Day 2:** Working with CSV files
- **Day 3:** Working with JSON files
- **Day 4:** Error handling with files
- **Day 5:** Mini-project: Simple file-based database

### Week 2: Code Organization
- **Day 6:** Organizing code into modules
- **Day 7:** Importing modules and functions
- **Day 8:** Creating a package
- **Day 9:** Introduction to virtual environments
- **Day 10:** Mini-project: Modular program

### Week 3: Expense Tracker Project
- **Day 11-15:** Build the Expense Tracker application

---

## 📁 Project Structure

```
phase_2_expense_tracker/
├── README.md               # This file
├── lessons/
│   ├── day_01_text_files/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_02_csv_files/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_03_json_files/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_04_file_errors/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_05_file_database/
│   │   ├── README.md
│   │   ├── database.py
│   │   └── test_database.py
│   ├── day_06_modules/
│   │   ├── README.md
│   │   └── exercises/
│   ├── day_07_imports/
│   │   ├── README.md
│   │   └── exercises/
│   ├── day_08_packages/
│   │   ├── README.md
│   │   └── my_package/
│   ├── day_09_virtualenv/
│   │   ├── README.md
│   │   └── exercises.py
│   └── day_10_modular_program/
│       ├── README.md
│       └── my_program/
├── project_expense_tracker/
│   ├── README.md
│   ├── expense_tracker.py    # Main application
│   ├── data/
│   │   ├── expenses.csv     # Sample data
│   │   └── expenses.json    # Sample data
│   ├── models/
│   │   ├── __init__.py
│   │   ├── expense.py       # Expense model
│   │   └── category.py      # Category model
│   ├── services/
│   │   ├── __init__.py
│   │   ├── file_service.py  # File operations
│   │   └── report_service.py # Report generation
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py       # Utility functions
│   └── tests/
│       └── test_tracker.py
├── resources/
│   ├── file_io_cheat_sheet.md
│   ├── csv_guide.md
│   ├── json_guide.md
│   └── code_organization.md
└── checklist.md            # Skills validation checklist
```

---

## 🚀 Getting Started

### Prerequisites
- ✅ Completed Phase 1 (Pure Python Fundamentals)
- ✅ Python 3.10+ installed
- ✅ Code editor (VS Code recommended)
- ✅ Basic terminal/command prompt knowledge

### Setup

```bash
# Navigate to the phase_2_expense_tracker folder
cd /workspace/python_learning_journey/phase_2_expense_tracker

# Create a folder for your work
mkdir -p my_work

# Start with Day 1
cd lessons/day_01_text_files
```

---

## 🎓 Daily Learning Approach

Each day follows this structure:

1. **Read the Lesson** (10-15 minutes)
   - Read the README.md file for the day
   - Understand the concepts

2. **Watch/Read Optional Resources** (5-10 minutes)
   - Links to videos, tutorials, and documentation

3. **Complete the Exercises** (20-40 minutes)
   - Work through the exercise files
   - Apply what you've learned

4. **Review and Reflect** (5-10 minutes)
   - Check your understanding
   - Review any mistakes
   - Ask questions if needed

5. **Practice** (Optional)
   - Additional challenges to reinforce learning

---

## 📚 Week 1: File Operations

### Day 1: Reading and Writing Text Files

**Learning Objectives:**
- Understand file paths (absolute vs. relative)
- Read from text files using `open()` and `read()`
- Write to text files using `open()` and `write()`
- Use the `with` statement for automatic file closing
- Understand file modes (`r`, `w`, `a`, `r+`, etc.)

**Exercises:**
- Read a text file and display its contents
- Write user input to a text file
- Append to an existing text file
- Count lines, words, and characters in a file

---

### Day 2: Working with CSV Files

**Learning Objectives:**
- Understand CSV (Comma-Separated Values) format
- Read CSV files using the `csv` module
- Write CSV files using the `csv` module
- Handle CSV files with different delimiters
- Work with CSV files that have headers

**Exercises:**
- Read a CSV file and display its contents
- Write data to a CSV file
- Parse CSV data into Python data structures
- Handle CSV files with different formats

---

### Day 3: Working with JSON Files

**Learning Objectives:**
- Understand JSON (JavaScript Object Notation) format
- Read JSON files using the `json` module
- Write JSON files using the `json` module
- Convert between Python objects and JSON
- Handle JSON data with different structures

**Exercises:**
- Read a JSON file and display its contents
- Write Python data to a JSON file
- Parse JSON data into Python objects
- Handle nested JSON structures

---

### Day 4: Error Handling with Files

**Learning Objectives:**
- Understand common file-related errors
- Use `try/except` blocks to handle file errors
- Handle `FileNotFoundError`, `PermissionError`, `IOError`
- Create robust file operations that don't crash
- Provide user-friendly error messages

**Exercises:**
- Handle file not found errors
- Handle permission errors
- Create a function that safely reads a file
- Create a function that safely writes to a file

---

### Day 5: Mini-Project - Simple File-Based Database

**Project:** Build a simple file-based database that can:
- Store records in a CSV or JSON file
- Add new records
- View all records
- Search for records
- Delete records

**Skills Practiced:**
- File I/O operations
- CSV and/or JSON file handling
- Error handling
- User input validation

---

## 📚 Week 2: Code Organization

### Day 6: Organizing Code into Modules

**Learning Objectives:**
- Understand what modules are
- Create your own modules
- Import modules into other files
- Understand the Python module search path
- Use relative and absolute imports

**Exercises:**
- Create a module with utility functions
- Import and use the module in another file
- Organize related functions into modules
- Understand `__name__ == "__main__"`

---

### Day 7: Importing Modules and Functions

**Learning Objectives:**
- Import entire modules
- Import specific functions from modules
- Use `as` to create aliases for imports
- Import everything from a module (not recommended)
- Understand the difference between `import module` and `from module import function`

**Exercises:**
- Import and use standard library modules
- Import and use your own modules
- Create and use module aliases
- Organize imports effectively

---

### Day 8: Creating a Package

**Learning Objectives:**
- Understand what packages are
- Create your own package
- Use `__init__.py` files
- Import from packages
- Understand package hierarchy

**Exercises:**
- Create a package with multiple modules
- Import from your package
- Organize related modules into packages
- Understand relative imports in packages

---

### Day 9: Introduction to Virtual Environments

**Learning Objectives:**
- Understand what virtual environments are
- Create virtual environments using `venv`
- Activate and deactivate virtual environments
- Install packages in a virtual environment
- Understand why virtual environments are useful

**Exercises:**
- Create a virtual environment
- Activate the virtual environment
- Install packages in the virtual environment
- Use the virtual environment for a project

---

### Day 10: Mini-Project - Modular Program

**Project:** Build a modular program that:
- Is organized into multiple modules
- Has a main module that imports from other modules
- Uses functions from different modules
- Can be run as a standalone application

**Skills Practiced:**
- Module creation and organization
- Importing between modules
- Code organization
- Project structure

---

## 🎯 Week 3: Expense Tracker Project

**Project:** Build a **Personal Expense Tracker** that allows users to:
- Add income and expense transactions
- Categorize transactions (Food, Transportation, Entertainment, etc.)
- View all transactions
- View transactions by category
- View summary statistics (total income, total expenses, balance)
- Save transactions to CSV and JSON files
- Load transactions from CSV and JSON files

### Project Structure

```
project_expense_tracker/
├── README.md               # Project documentation
├── expense_tracker.py     # Main application (command-line interface)
├── data/
│   ├── expenses.csv       # Sample CSV data
│   └── expenses.json      # Sample JSON data
├── models/
│   ├── __init__.py
│   ├── expense.py         # Expense model (data structure)
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

### Project Milestones

#### Milestone 1: Project Setup and Data Models
- Create the project structure
- Define data models for expenses and categories
- Create basic utility functions

#### Milestone 2: File Services
- Implement CSV file reading/writing
- Implement JSON file reading/writing
- Create functions to save/load transactions

#### Milestone 3: Core Functionality
- Implement transaction CRUD operations
- Implement category management
- Implement summary statistics

#### Milestone 4: User Interface
- Create the command-line interface
- Implement menu system
- Handle user input
- Display formatted output

#### Milestone 5: Testing and Polish
- Test all functionality
- Fix any bugs
- Add error handling
- Improve user experience

---

## 💡 Tips for Success

### 1. Practice File Operations
- Create test files to practice reading/writing
- Experiment with different file modes
- Practice error handling with files

### 2. Organize Your Code
- Group related functions together
- Use descriptive module names
- Keep modules focused on one purpose
- Follow the DRY principle

### 3. Handle Errors Gracefully
- Always use try/except for file operations
- Provide user-friendly error messages
- Don't let your program crash

### 4. Test Your Code
- Test with different file types
- Test error cases (missing files, permissions, etc.)
- Test edge cases (empty files, large files, etc.)

### 5. Document Your Code
- Add docstrings to functions
- Add comments for complex logic
- Document your modules

---

## 📚 Additional Resources

### File I/O
- [Python Documentation - File Objects](https://docs.python.org/3/glossary.html#term-file-object)
- [Python Documentation - open()](https://docs.python.org/3/library/functions.html#open)
- [Real Python - Reading and Writing Files](https://realpython.com/read-write-files-python/)
- [Real Python - Working with Files](https://realpython.com/python-read-text-file/)

### CSV
- [Python Documentation - csv module](https://docs.python.org/3/library/csv.html)
- [Real Python - CSV Files](https://realpython.com/python-csv/)
- [CSV Format Specification](https://tools.ietf.org/html/rfc4180)

### JSON
- [Python Documentation - json module](https://docs.python.org/3/library/json.html)
- [Real Python - JSON in Python](https://realpython.com/python-json/)
- [JSON Official Website](https://www.json.org/json-en.html)

### Code Organization
- [Python Documentation - Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Documentation - Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Real Python - Python Modules and Imports](https://realpython.com/absolute-vs-relative-python-imports/)
- [Real Python - Python Packages](https://realpython.com/python-modules-and-packages/)

### Virtual Environments
- [Python Documentation - venv](https://docs.python.org/3/library/venv.html)
- [Real Python - Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Virtual Environment Tutorial](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

---

## 🎉 Phase Completion Checklist

Before moving to Phase 3, make sure you can:

- [ ] Read from and write to text files
- [ ] Work with CSV files using the csv module
- [ ] Work with JSON files using the json module
- [ ] Handle file-related errors gracefully
- [ ] Use context managers (with statement) for file operations
- [ ] Organize code into multiple modules
- [ ] Import and use code from different files
- [ ] Create and use packages
- [ ] Use virtual environments
- [ ] Build a complete application with file persistence

**Validation:** Complete all daily exercises and the Expense Tracker project.

---

## 🚀 Next Steps

Once you've completed Phase 2:
1. Review the checklist in `checklist.md`
2. Make sure you understand all the concepts
3. Move on to **Phase 3: Entering the Web (Python + HTML/CSS)**

**Ready to begin?** Start with `lessons/day_01_text_files/README.md`!
