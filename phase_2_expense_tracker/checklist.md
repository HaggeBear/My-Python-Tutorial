# Phase 2: Data Persistence & Organization - Checklist

## 🎯 Phase Completion Checklist

Before moving to Phase 3, make sure you've completed all the requirements below.
Check off each item as you complete it.

---

## ✅ Week 1: File Operations

### Day 1: Reading and Writing Text Files
- [ ] I understand file paths (absolute vs. relative)
- [ ] I can read from text files using `open()` and `read()`
- [ ] I can write to text files using `open()` and `write()`
- [ ] I understand the `with` statement for automatic file closing
- [ ] I understand file modes (`r`, `w`, `a`, `r+`, etc.)
- [ ] I can read a file line by line
- [ ] I can write multiple lines to a file
- [ ] I can append to an existing file

**Exercises:**
- [ ] Completed `lessons/day_01_text_files/exercises.py`

---

### Day 2: Working with CSV Files
- [ ] I understand CSV (Comma-Separated Values) format
- [ ] I can read CSV files using the `csv` module
- [ ] I can write CSV files using the `csv` module
- [ ] I can handle CSV files with different delimiters
- [ ] I can work with CSV files that have headers
- [ ] I understand `csv.reader` and `csv.writer`
- [ ] I understand `csv.DictReader` and `csv.DictWriter`

**Exercises:**
- [ ] Completed `lessons/day_02_csv_files/exercises.py`

---

### Day 3: Working with JSON Files
- [ ] I understand JSON (JavaScript Object Notation) format
- [ ] I can read JSON files using the `json` module
- [ ] I can write JSON files using the `json` module
- [ ] I can convert between Python objects and JSON
- [ ] I can handle JSON data with different structures
- [ ] I understand `json.dump()` and `json.dump()`
- [ ] I understand `json.load()` and `json.loads()`

**Exercises:**
- [ ] Completed `lessons/day_03_json_files/exercises.py`

---

### Day 4: Error Handling with Files
- [ ] I understand common file-related errors
- [ ] I can use `try/except` blocks to handle file errors
- [ ] I can handle `FileNotFoundError`
- [ ] I can handle `PermissionError`
- [ ] I can handle `IOError`
- [ ] I can create robust file operations that don't crash
- [ ] I can provide user-friendly error messages

**Exercises:**
- [ ] Completed `lessons/day_04_file_errors/exercises.py`

---

### Day 5: Mini-Project - Simple File-Based Database
- [ ] I can store records in a CSV or JSON file
- [ ] I can add new records to the database
- [ ] I can view all records from the database
- [ ] I can search for records in the database
- [ ] I can delete records from the database
- [ ] I can handle file errors gracefully

**Project:**
- [ ] Completed `lessons/day_05_file_database/database.py`
- [ ] Completed `lessons/day_05_file_database/test_database.py`

---

## ✅ Week 2: Code Organization

### Day 6: Organizing Code into Modules
- [ ] I understand what modules are
- [ ] I can create my own modules
- [ ] I can import modules into other files
- [ ] I understand the Python module search path
- [ ] I can use relative and absolute imports
- [ ] I understand `__name__ == "__main__"`

**Exercises:**
- [ ] Completed `lessons/day_06_modules/exercises/`

---

### Day 7: Importing Modules and Functions
- [ ] I can import entire modules
- [ ] I can import specific functions from modules
- [ ] I can use `as` to create aliases for imports
- [ ] I understand the difference between `import module` and `from module import function`
- [ ] I can organize imports effectively

**Exercises:**
- [ ] Completed `lessons/day_07_imports/exercises/`

---

### Day 8: Creating a Package
- [ ] I understand what packages are
- [ ] I can create my own package
- [ ] I understand `__init__.py` files
- [ ] I can import from packages
- [ ] I understand package hierarchy
- [ ] I can use relative imports in packages

**Exercises:**
- [ ] Completed `lessons/day_08_packages/my_package/`

---

### Day 9: Introduction to Virtual Environments
- [ ] I understand what virtual environments are
- [ ] I can create virtual environments using `venv`
- [ ] I can activate and deactivate virtual environments
- [ ] I can install packages in a virtual environment
- [ ] I understand why virtual environments are useful

**Exercises:**
- [ ] Completed `lessons/day_09_virtualenv/exercises.py`

---

### Day 10: Mini-Project - Modular Program
- [ ] I can organize a program into multiple modules
- [ ] I can create a main module that imports from other modules
- [ ] I can use functions from different modules
- [ ] I can run the program as a standalone application

**Project:**
- [ ] Completed `lessons/day_10_modular_program/my_program/`

---

## ✅ Week 3: Expense Tracker Project

### Project Structure
- [ ] Created the project directory structure
- [ ] Created `__init__.py` files for packages
- [ ] Created all necessary Python files

### Milestone 1: Project Setup and Data Models
- [ ] Created `models/expense.py` with Expense class
- [ ] Created `models/category.py` with Category class
- [ ] Created `utils/helpers.py` with utility functions
- [ ] Tested that classes can be instantiated
- [ ] Tested that utility functions work correctly

### Milestone 2: File Services
- [ ] Implemented `save_expenses_to_csv()`
- [ ] Implemented `load_expenses_from_csv()`
- [ ] Implemented `save_expenses_to_json()`
- [ ] Implemented `load_expenses_from_json()`
- [ ] Implemented `save_categories_to_json()`
- [ ] Implemented `load_categories_from_json()`
- [ ] Created sample CSV and JSON files
- [ ] Tested all file operations

### Milestone 3: Core Functionality
- [ ] Implemented `get_summary_statistics()`
- [ ] Implemented `get_expenses_by_category()`
- [ ] Implemented `get_category_totals()`
- [ ] Implemented `get_expenses_by_month()`
- [ ] Implemented `get_monthly_totals()`
- [ ] Tested all reporting functions

### Milestone 4: User Interface
- [ ] Created the main application file (`expense_tracker.py`)
- [ ] Implemented the menu system
- [ ] Implemented all user interaction functions
- [ ] Connected all services to the UI
- [ ] Tested the complete application

### Milestone 5: Testing and Polish
- [ ] Tested all functionality thoroughly
- [ ] Fixed any bugs found
- [ ] Added error handling where missing
- [ ] Improved user experience
- [ ] Cleaned up the code

**Project:**
- [ ] Completed all milestones in `project_expense_tracker/README.md`

---

## 🎯 Skills Validation

### Conceptual Understanding

Test your understanding by answering these questions:

1. What is the difference between reading a file in text mode vs. binary mode?
   - Your answer: ________________________________________

2. What are the main differences between CSV and JSON file formats?
   - Your answer: ________________________________________

3. What is a context manager and why is it useful for file operations?
   - Your answer: ________________________________________

4. What is the difference between a module and a package in Python?
   - Your answer: ________________________________________

5. What is a virtual environment and why would you use one?
   - Your answer: ________________________________________

6. What is the Python module search path?
   - Your answer: ________________________________________

7. What is the difference between absolute and relative imports?
   - Your answer: ________________________________________

8. How do you handle a FileNotFoundError in Python?
   - Your answer: ________________________________________

### Practical Skills

- [ ] I can read from and write to text files
- [ ] I can work with CSV files using the csv module
- [ ] I can work with JSON files using the json module
- [ ] I can handle file-related errors gracefully
- [ ] I can use context managers for file operations
- [ ] I can organize code into multiple modules
- [ ] I can import and use code from different files
- [ ] I can create and use packages
- [ ] I can use virtual environments
- [ ] I can build a complete application with file persistence

---

## 📝 Knowledge Check Answers

Write your answers to the conceptual understanding questions above.

---

## 🎉 Phase Completion

**Before moving to Phase 3, make sure:**

1. [ ] All daily exercises are complete
2. [ ] All mini-projects are complete
3. [ ] The Expense Tracker project is complete
4. [ ] I understand all the concepts in Phase 2
5. [ ] I can work with files (text, CSV, JSON) confidently
6. [ ] I can organize code into modules and packages
7. [ ] I can handle file errors gracefully

**If you can check all of these, you're ready for Phase 3!**

---

## 🚀 Next Steps

Once you've completed Phase 2:
1. Review the checklist one more time
2. Celebrate your accomplishment! 🎉
3. Move on to **Phase 3: Entering the Web (Python + HTML/CSS)**

---

## 📚 Additional Practice (Optional)

If you want more practice before moving on:

1. **File I/O Practice:**
   - Create a log file analyzer
   - Build a text-based database for any data you're interested in
   - Create a file encryption/decryption tool

2. **Code Organization Practice:**
   - Refactor an existing program into multiple modules
   - Create a utility package with reusable functions
   - Build a larger application with proper package structure

3. **Projects:**
   - Build a personal journal application
   - Create a recipe book with file storage
   - Build a simple inventory management system
   - Create a quiz game that loads questions from a file

---

## 💬 Reflection Questions

Take a moment to reflect on your learning:

1. What was the most challenging concept in Phase 2?
   - Your answer: ________________________________________

2. What concept do you feel most confident about?
   - Your answer: ________________________________________

3. What was your favorite project or exercise?
   - Your answer: ________________________________________

4. What do you want to learn more about in Phase 3?
   - Your answer: ________________________________________

---

**Great job on completing Phase 2!** 🎉

*Checklist last updated: [Date]*
*Phase 2 Status: [ ] In Progress  [ ] Complete
