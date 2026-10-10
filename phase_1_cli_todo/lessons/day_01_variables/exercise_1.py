# Day 1: Variables and Data Types - Exercise 1
# ================================================

"""
Exercise 1: Variable Creation and Naming

In this exercise, you'll practice creating variables and following
Python naming conventions.

Instructions:
1. Create variables as described in each task
2. Use proper naming conventions (PEP 8)
3. Run the code to verify it works
4. Check that the output matches the expected output

HINT: If you get a NameError, make sure you've created the variable before using it.
"""

# --- TASK 1: Create Basic Variables ---
# Create variables to store the following information:
# - Your first name (string)
# - Your age (integer)
# - Your height in meters (float)
# - Whether you're a student (boolean - True or False)

# Your code here:
# first_name = ""
# age = 
# height = 
# is_student = 

# Test your variables
print("Task 1:")
print(f"Name: {first_name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")

# Expected output (with your values):
# Name: [your name]
# Age: [your age]
# Height: [your height]
# Is student: True or False

# --- TASK 2: Variable Naming Practice ---
# Fix the following variable names to follow PEP 8 conventions:

# Bad names - fix these!
userName = "Alice"  # Should be snake_case
UserAge = 25        # Should be lowercase
TOTAL_SCORE = 100   # This is actually correct for a constant!
first_name1 = "Bob" # Not very descriptive

# Your fixed code here:
# user_name = "Alice"
# user_age = 25
# TOTAL_SCORE = 100  # This one is fine
# full_name = "Bob"  # More descriptive

# Test your fixed names
print("\nTask 2:")
print(f"Username: {user_name}")
print(f"User age: {user_age}")
print(f"Total score: {TOTAL_SCORE}")
print(f"Full name: {full_name}")

# Expected output:
# Username: Alice
# User age: 25
# Total score: 100
# Full name: Bob

# --- TASK 3: Multiple Assignments ---
# Python allows you to assign multiple variables in one line.
# Use this feature to create three variables in one line:
# - x = 10
# - y = 20
# - z = 30

# Your code here:
# x, y, z = 

# Test your variables
print("\nTask 3:")
print(f"x = {x}, y = {y}, z = {z}")

# Expected output:
# x = 10, y = 20, z = 30

# --- TASK 4: Swapping Variables ---
# Swap the values of a and b using Python's multiple assignment feature

a = 5
b = 10

# Your code here:
# a, b = 

# Test your variables
print("\nTask 4:")
print(f"a = {a}, b = {b}")

# Expected output:
# a = 10, b = 5

# --- TASK 5: Constants ---
# Create constants for the following (use UPPERCASE names):
# - The value of pi (3.14159)
# - The speed of light in m/s (299792458)
# - The number of days in a week (7)

# Your code here:
# PI = 
# SPEED_OF_LIGHT = 
# DAYS_IN_WEEK = 

# Test your constants
print("\nTask 5:")
print(f"PI: {PI}")
print(f"Speed of light: {SPEED_OF_LIGHT} m/s")
print(f"Days in week: {DAYS_IN_WEEK}")

# Expected output:
# PI: 3.14159
# Speed of light: 299792458 m/s
# Days in week: 7

# --- FINAL TEST ---
# If all tasks are correct, the output should look like:
# Task 1:
# Name: [your name]
# Age: [your age]
# Height: [your height]
# Is student: True or False
#
# Task 2:
# Username: Alice
# User age: 25
# Total score: 100
# Full name: Bob
#
# Task 3:
# x = 10, y = 20, z = 30
#
# Task 4:
# a = 10, b = 5
#
# Task 5:
# PI: 3.14159
# Speed of light: 299792458 m/s
# Days in week: 7

print("\n✅ All tasks in Exercise 1 complete!")
