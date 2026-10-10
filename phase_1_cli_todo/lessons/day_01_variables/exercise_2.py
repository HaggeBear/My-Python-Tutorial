# Day 1: Variables and Data Types - Exercise 2
# ================================================

"""
Exercise 2: Data Types and Type Conversion

In this exercise, you'll practice working with different data types
and converting between them.

Instructions:
1. Create variables of different types
2. Use the type() function to check types
3. Convert between types
4. Run the code to verify it works

HINT: Use int(), float(), str(), and bool() for type conversion.
"""

# --- TASK 1: Create Variables of Different Types ---
# Create one variable for each of the following types:
# - Integer
# - Float
# - String
# - Boolean

# Your code here:
# my_integer = 
# my_float = 
# my_string = 
# my_boolean = 

# Check the types
print("Task 1:")
print(f"my_integer type: {type(my_integer)}")
print(f"my_float type: {type(my_float)}")
print(f"my_string type: {type(my_string)}")
print(f"my_boolean type: {type(my_boolean)}")

# Expected output:
# my_integer type: <class 'int'>
# my_float type: <class 'float'>
# my_string type: <class 'str'>
# my_boolean type: <class 'bool'>

# --- TASK 2: Type Conversion ---
# Convert the following variables to different types:

# Starting variables
num_str = "42"
num_int = 42
num_float = 42.5

# Convert num_str to integer
# num_str_to_int = 

# Convert num_str to float
# num_str_to_float = 

# Convert num_int to string
# num_int_to_str = 

# Convert num_int to float
# num_int_to_float = 

# Convert num_float to integer (loses decimal part)
# num_float_to_int = 

# Convert num_float to string
# num_float_to_str = 

# Test your conversions
print("\nTask 2:")
print(f"String to int: {num_str_to_int}, type: {type(num_str_to_int)}")
print(f"String to float: {num_str_to_float}, type: {type(num_str_to_float)}")
print(f"Int to string: {num_int_to_str}, type: {type(num_int_to_str)}")
print(f"Int to float: {num_int_to_float}, type: {type(num_int_to_float)}")
print(f"Float to int: {num_float_to_int}, type: {type(num_float_to_int)}")
print(f"Float to string: {num_float_to_str}, type: {type(num_float_to_str)}")

# Expected output:
# String to int: 42, type: <class 'int'>
# String to float: 42.0, type: <class 'float'>
# Int to string: 42, type: <class 'str'>
# Int to float: 42.0, type: <class 'float'>
# Float to int: 42, type: <class 'int'>
# Float to string: 42.5, type: <class 'str'>

# --- TASK 3: Automatic Type Conversion ---
# Test what happens when you mix different numeric types

# Integer + Float
result1 = 5 + 3.14
print("\nTask 3:")
print(f"5 + 3.14 = {result1}, type: {type(result1)}")

# Integer + Integer
result2 = 5 + 3
print(f"5 + 3 = {result2}, type: {type(result2)}")

# Float + Float
result3 = 3.14 + 2.71
print(f"3.14 + 2.71 = {result3}, type: {type(result3)}")

# Expected output:
# 5 + 3.14 = 8.14, type: <class 'float'>
# 5 + 3 = 8, type: <class 'int'>
# 3.14 + 2.71 = 5.85, type: <class 'float'>

# --- TASK 4: Boolean Conversion ---
# Test what values convert to True or False

# Test these values with bool()
test_values = [0, 1, -1, "", "hello", [], [1, 2, 3], None, True, False]

print("\nTask 4:")
for value in test_values:
    print(f"bool({value!r}) = {bool(value)}")

# Expected output:
# bool(0) = False
# bool(1) = True
# bool(-1) = True
# bool('') = False
# bool('hello') = True
# bool([]) = False
# bool([1, 2, 3]) = True
# bool(None) = False
# bool(True) = True
# bool(False) = False

# --- TASK 5: String Formatting with Different Types ---
# Create a formatted string that includes all four data types

# Your variables from Task 1
# my_integer = 42
# my_float = 3.14
# my_string = "Hello"
# my_boolean = True

# Create a formatted string that includes all four
# formatted_string = 

print("\nTask 5:")
print(f"Formatted string: {formatted_string}")

# Expected output (example):
# Formatted string: Integer: 42, Float: 3.14, String: Hello, Boolean: True

# --- TASK 6: Type Checking Function ---
# Write a function that takes a value and prints its type

# Your code here:
# def print_type(value):
#     """Print the type of the given value."""
#     

print("\nTask 6:")
print_type(42)
print_type(3.14)
print_type("Hello")
print_type(True)

# Expected output:
# Type of 42: <class 'int'>
# Type of 3.14: <class 'float'>
# Type of Hello: <class 'str'>
# Type of True: <class 'bool'>

# --- FINAL TEST ---
# If all tasks are correct, you should see the expected outputs above.

print("\n✅ All tasks in Exercise 2 complete!")
