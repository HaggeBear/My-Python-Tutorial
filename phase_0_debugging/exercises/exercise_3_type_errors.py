# Exercise 3: Type Errors
# ========================

"""
In this exercise, you'll practice identifying and fixing TypeError.

A TypeError occurs when you try to perform an operation on incompatible types.
For example, you can't add a string and an integer directly.

Instructions:
1. Read the error message carefully
2. Identify which operation is causing the problem
3. Think about the types involved
4. Fix the error by converting types or using appropriate operations
5. Run the code to verify it works

There are 5 TypeErrors in this file. Fix them all!

HINT: Use type() to check variable types if you're unsure.
      Use int(), float(), str() to convert between types.
"""

# --- ERROR 1: Adding string and integer ---
# You can't directly add a string and an integer

x = "10"
y = 5
result = x + y  # TypeError: can only concatenate str (not "int") to str

# Fix: Convert x to integer first

# --- ERROR 2: Using string methods on non-string ---
# .upper() only works on strings

number = 42
upper_number = number.upper()  # TypeError: 'int' object has no attribute 'upper'

# Fix: Convert number to string first, or remove the .upper() call

# --- ERROR 3: Concatenating different types in print ---
# print() can handle different types, but string concatenation requires same types

name = "Alice"
age = 30
message = "Name: " + name + ", Age: " + age  # TypeError

# Fix: Convert age to string

# --- ERROR 4: Using list methods on non-list ---
# .append() only works on lists

my_tuple = (1, 2, 3)
my_tuple.append(4)  # TypeError: 'tuple' object has no attribute 'append'

# Fix: Convert to list first, or use tuple concatenation

# --- ERROR 5: Division with incompatible types ---
# Can't divide string by integer

total_str = "100"
count = 5
average = total_str / count  # TypeError: unsupported operand type(s)

# Fix: Convert total_str to float or int

# --- TEST YOUR CODE ---
# If you've fixed all the errors, the output should be:
# 15
# 42 (or "42" depending on your fix)
# Name: Alice, Age: 30
# [1, 2, 3, 4] (or similar)
# 20.0 (or 20 depending on your fix)
# All type errors fixed! ✅

print("\nAll type errors fixed! ✅")
