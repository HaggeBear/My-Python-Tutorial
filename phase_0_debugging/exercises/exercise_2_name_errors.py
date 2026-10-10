# Exercise 2: Name Errors
# ========================

"""
In this exercise, you'll practice identifying and fixing NameError.

A NameError occurs when you try to use a variable or function that hasn't been defined.
Python doesn't know what you're referring to.

Instructions:
1. Read the error message carefully
2. Identify which variable name is causing the problem
3. Think about why Python doesn't recognize that name
4. Fix the error by defining the variable or fixing the name
5. Run the code to verify it works

There are 5 NameErrors in this file. Fix them all!

HINT: Common causes of NameError:
- Misspelled variable name
- Forgot to define a variable
- Variable is out of scope
- Forgot to import a module
"""

# --- ERROR 1: Using variable before definition ---
# The error will say: NameError: name 'result' is not defined

print(result)  # We're trying to print result before defining it
result = 10 + 5

# Fix: Define the variable before using it

# --- ERROR 2: Misspelled variable name ---
# Look closely at the variable names

name = "Alice"
print(naem)  # Oops, typo!

# Fix: Correct the spelling

# --- ERROR 3: Using a variable outside its scope ---
# Variables defined inside a function are not available outside

def calculate():
    total = 10 + 20

print(total)  # total is not defined here

# Fix: Either define total outside the function, or return it

# --- ERROR 4: Forgot to import module ---
# We're trying to use random.randint but haven't imported random

number = random.randint(1, 10)
print("Random number:", number)

# Fix: Add the import statement at the top

# --- ERROR 5: Function called before definition ---
# We're calling a function before we've defined it

say_hello()

def say_hello():
    print("Hello!")

# Fix: Move the function definition before the call

# --- TEST YOUR CODE ---
# If you've fixed all the errors, the output should be:
# 15
# Alice
# 30
# Random number: [some number between 1 and 10]
# Hello!
# All name errors fixed! ✅

print("\nAll name errors fixed! ✅")
