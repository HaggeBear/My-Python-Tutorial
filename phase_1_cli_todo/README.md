# Phase 1: Pure Python Fundamentals (The Terminal Era) 🐍

## 🎯 Phase Overview

**Welcome to Phase 1!** Now that you've learned how to debug, it's time to start writing Python code.

In this phase, you'll learn the **fundamentals of Python programming** by building a **Command-Line Todo List Application**. This project will teach you the core concepts that every Python programmer needs to know.

---

## 📚 Learning Goals

By the end of this phase, you will be able to:

- ✅ Use variables and understand data types (strings, integers, floats, booleans)
- ✅ Get user input and produce output in the terminal
- ✅ Use basic operators (arithmetic, comparison, logical)
- ✅ Write conditional statements (if/elif/else)
- ✅ Write loops (for and while)
- ✅ Create and use lists, tuples, dictionaries, and sets
- ✅ Write functions with parameters and return values
- ✅ Handle user input validation
- ✅ Build a complete command-line application

---

## 🗺️ Phase Roadmap

### Week 1: Variables, Input/Output, and Basic Operations
- **Day 1:** Variables and data types
- **Day 2:** User input and output
- **Day 3:** Basic operators
- **Day 4:** Mini-project: Simple calculator

### Week 2: Control Flow
- **Day 5:** Conditional statements (if/elif/else)
- **Day 6:** Boolean logic
- **Day 7:** The for loop
- **Day 8:** The while loop
- **Day 9:** Mini-project: Number guessing game

### Week 3: Data Structures
- **Day 10:** Lists and list methods
- **Day 11:** Tuples
- **Day 12:** Dictionaries
- **Day 13:** Sets
- **Day 14:** Mini-project: Contact book

### Week 4: Functions and the Todo List Project
- **Day 15:** Defining functions
- **Day 16:** Function parameters and return values
- **Day 17:** Scope and lifetime of variables
- **Day 18-21:** Todo List Application project

---

## 📁 Project Structure

```
phase_1_cli_todo/
├── README.md               # This file
├── lessons/
│   ├── day_01_variables/
│   │   ├── README.md
│   │   ├── exercise_1.py
│   │   └── exercise_2.py
│   ├── day_02_input_output/
│   │   ├── README.md
│   │   ├── exercise_1.py
│   │   └── exercise_2.py
│   ├── day_03_operators/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_04_calculator/
│   │   ├── README.md
│   │   ├── calculator.py
│   │   └── test_calculator.py
│   ├── day_05_conditionals/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_06_boolean_logic/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_07_for_loops/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_08_while_loops/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_09_guessing_game/
│   │   ├── README.md
│   │   ├── guessing_game.py
│   │   └── test_guessing_game.py
│   ├── day_10_lists/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_11_tuples/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_12_dictionaries/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_13_sets/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_14_contact_book/
│   │   ├── README.md
│   │   ├── contact_book.py
│   │   └── test_contact_book.py
│   ├── day_15_functions/
│   │   ├── README.md
│   │   └── exercises.py
│   ├── day_16_function_parameters/
│   │   ├── README.md
│   │   └── exercises.py
│   └── day_17_scope/
│       ├── README.md
│       └── exercises.py
├── project_todo_list/
│   ├── README.md
│   ├── todo_list.py          # Main application
│   ├── requirements.txt
│   └── tests/
│       └── test_todo_list.py
├── resources/
│   ├── python_cheat_sheet.md
│   ├── best_practices.md
│   └── common_pitfalls.md
├── solutions/              # Reference solutions
│   └── ...
└── checklist.md            # Skills validation checklist
```

---

## 🚀 Getting Started

### Prerequisites
- ✅ Completed Phase 0 (Debugging Basics)
- ✅ Python 3.10+ installed
- ✅ Code editor (VS Code recommended)
- ✅ Terminal/command prompt

### Setup

```bash
# Navigate to the phase_1_cli_todo folder
cd /workspace/python_learning_journey/phase_1_cli_todo

# Create a folder for your work
mkdir -p my_work

# Start with Day 1
cd lessons/day_01_variables
```

---

## 🎓 Daily Learning Approach

Each day follows this structure:

1. **Read the Lesson** (10-15 minutes)
   - Read the README.md file for the day
   - Understand the concepts

2. **Watch/Read Optional Resources** (5-10 minutes)
   - Links to videos, tutorials, and documentation

3. **Complete the Exercises** (20-30 minutes)
   - Work through the exercise files
   - Apply what you've learned

4. **Review and Reflect** (5-10 minutes)
   - Check your understanding
   - Review any mistakes
   - Ask questions if needed

5. **Practice** (Optional)
   - Additional challenges to reinforce learning

---

## 📚 Day-by-Day Breakdown

### Week 1: Foundations

#### Day 1: Variables and Data Types
**Concepts:**
- What are variables?
- Integer, float, string, boolean data types
- Variable naming conventions (PEP 8)
- The `type()` function

**Exercises:**
- Create variables of different types
- Practice variable naming
- Convert between types

---

#### Day 2: User Input and Output
**Concepts:**
- The `print()` function
- The `input()` function
- String formatting (f-strings)
- Escape sequences

**Exercises:**
- Get user input and display output
- Format strings with f-strings
- Create a simple conversation program

---

#### Day 3: Basic Operators
**Concepts:**
- Arithmetic operators (+, -, *, /, //, %, **)
- Assignment operators (=, +=, -=, etc.)
- Comparison operators (==, !=, >, <, >=, <=)
- Operator precedence

**Exercises:**
- Perform calculations
- Use different operators
- Understand precedence

---

#### Day 4: Mini-Project - Simple Calculator
**Project:** Build a command-line calculator that can:
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers
- Handle user input and validation

**Skills Practiced:**
- Variables
- User input/output
- Arithmetic operators
- Basic error handling

---

### Week 2: Control Flow

#### Day 5: Conditional Statements
**Concepts:**
- `if` statements
- `elif` and `else` clauses
- Indentation in conditionals
- Truthy and falsy values

**Exercises:**
- Write conditional logic
- Use if/elif/else
- Test different conditions

---

#### Day 6: Boolean Logic
**Concepts:**
- `and`, `or`, `not` operators
- Boolean expressions
- Short-circuit evaluation
- Truth tables

**Exercises:**
- Combine conditions with and/or
- Use not to negate conditions
- Create complex boolean expressions

---

#### Day 7: The for Loop
**Concepts:**
- `for` loop syntax
- Looping over sequences (strings, lists, etc.)
- The `range()` function
- Nested for loops

**Exercises:**
- Loop over lists and strings
- Use range() with different parameters
- Create nested loops

---

#### Day 8: The while Loop
**Concepts:**
- `while` loop syntax
- Loop conditions
- Infinite loops and how to avoid them
- `break` and `continue` statements

**Exercises:**
- Write while loops with different conditions
- Use break and continue
- Avoid infinite loops

---

#### Day 9: Mini-Project - Number Guessing Game
**Project:** Build a number guessing game where:
- The computer picks a random number
- The user tries to guess it
- The computer gives hints (too high, too low)
- The game continues until the user guesses correctly

**Skills Practiced:**
- Random number generation
- While loops
- Conditional statements
- User input/output

---

### Week 3: Data Structures

#### Day 10: Lists
**Concepts:**
- Creating lists
- Accessing list elements
- List methods (append, remove, pop, etc.)
- List slicing
- List comprehensions (introduction)

**Exercises:**
- Create and manipulate lists
- Use list methods
- Practice list slicing

---

#### Day 11: Tuples
**Concepts:**
- Creating tuples
- Tuple immutability
- Accessing tuple elements
- When to use tuples vs. lists

**Exercises:**
- Create and use tuples
- Understand immutability
- Compare tuples and lists

---

#### Day 12: Dictionaries
**Concepts:**
- Creating dictionaries
- Accessing dictionary values by key
- Dictionary methods (keys, values, items, etc.)
- Adding, modifying, and removing key-value pairs
- Dictionary comprehensions (introduction)

**Exercises:**
- Create and manipulate dictionaries
- Use dictionary methods
- Practice accessing values

---

#### Day 13: Sets
**Concepts:**
- Creating sets
- Set operations (union, intersection, difference)
- Set methods (add, remove, etc.)
- When to use sets vs. lists

**Exercises:**
- Create and use sets
- Perform set operations
- Understand uniqueness

---

#### Day 14: Mini-Project - Contact Book
**Project:** Build a contact book that can:
- Add new contacts
- View all contacts
- Search for contacts
- Delete contacts

**Skills Practiced:**
- Lists and/or dictionaries
- Loops
- Conditional statements
- User input/output

---

### Week 4: Functions and Final Project

#### Day 15: Defining Functions
**Concepts:**
- Function syntax (`def`)
- Calling functions
- Function documentation (docstrings)
- Simple functions without parameters

**Exercises:**
- Define and call functions
- Write docstrings
- Organize code with functions

---

#### Day 16: Function Parameters and Return Values
**Concepts:**
- Function parameters
- Return values
- Multiple return values
- Default parameter values
- Named arguments

**Exercises:**
- Write functions with parameters
- Return values from functions
- Use default parameters

---

#### Day 17: Scope and Lifetime of Variables
**Concepts:**
- Local vs. global scope
- The `global` keyword
- Variable lifetime
- Function scope

**Exercises:**
- Understand variable scope
- Use global variables appropriately
- Avoid scope-related bugs

---

#### Days 18-21: Todo List Application Project
**Project:** Build a complete command-line todo list application with:
- Add tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Save tasks to a file
- Load tasks from a file

**Skills Practiced:**
- All concepts from Phase 1
- File I/O (introduction to Phase 2 concepts)
- Code organization
- User experience

---

## 🎯 Project-Based Learning

The **Todo List Application** is the capstone project for Phase 1. It will bring together everything you've learned:

1. **Variables and Data Types:** Storing task information
2. **Input/Output:** Getting user commands and displaying tasks
3. **Conditionals:** Handling different user commands
4. **Loops:** Displaying all tasks, main program loop
5. **Lists:** Storing the list of tasks
6. **Dictionaries:** Storing task details (description, status, etc.)
7. **Functions:** Organizing code into reusable pieces

---

## 💡 Tips for Success

### 1. Take Notes
- Write down new concepts
- Note examples that help you understand
- Keep a list of questions

### 2. Practice Daily
- Even 20-30 minutes helps
- Consistency is key
- Code a little every day

### 3. Don't Just Copy
- Type out code yourself
- Modify examples to see what happens
- Break things to understand them

### 4. Debug Often
- Use the skills from Phase 0
- Read error messages carefully
- Add print statements to see what's happening

### 5. Ask Questions
- If you don't understand something, ask!
- Explain what you've tried
- Show your code
- Be specific about what's confusing

---

## 📚 Additional Resources

### Free Interactive Tutorials
- [Python for Beginners (Microsoft)](https://learn.microsoft.com/en-us/training/modules/intro-to-python/)
- [Python.org Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Real Python Tutorials](https://realpython.com/)
- [W3Schools Python](https://www.w3schools.com/python/)

### Video Courses
- [Python for Beginners (freeCodeCamp)](https://www.youtube.com/watch?v=rfscVS0vtbw)
- [CS50's Introduction to Programming with Python (Harvard)](https://cs50.harvard.edu/python/2022/)

### Practice Platforms
- [Exercism Python Track](https://exercism.org/tracks/python)
- [Codewars Python Katas](https://www.codewars.com/?language=python)
- [LeetCode Easy Python Problems](https://leetcode.com/problemset/all/?difficulty=EASY&page=1&listId=wpwgkgt)

---

## 🎉 Phase Completion Checklist

Before moving to Phase 2, make sure you can:

- [ ] Create and use variables of different types
- [ ] Get user input and display output
- [ ] Use arithmetic, comparison, and logical operators
- [ ] Write conditional statements (if/elif/else)
- [ ] Write for and while loops
- [ ] Create and manipulate lists, tuples, dictionaries, and sets
- [ ] Define and call functions with parameters and return values
- [ ] Understand variable scope
- [ ] Build a complete command-line application
- [ ] Debug your code effectively

**Validation:** Complete all daily exercises and the Todo List project.

---

## 🚀 Next Steps

Once you've completed Phase 1:
1. Review the checklist in `checklist.md`
2. Make sure you understand all the concepts
3. Move on to **Phase 2: Data Persistence & Organization**

**Ready to begin?** Start with `lessons/day_01_variables/README.md`!
