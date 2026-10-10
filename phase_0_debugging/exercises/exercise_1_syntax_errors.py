# Exercise 1: Syntax Errors
# ===========================

"""
In this exercise, you'll practice identifying and fixing syntax errors.

Syntax errors are problems with the structure of your code that prevent Python
from even trying to run it. Python will point you to the exact line where it
encountered the problem.

Instructions:
1. Read the error message carefully
2. Identify which line has the error
3. Look at the line and think about what's wrong
4. Fix the error
5. Run the code to verify it works

There are 5 syntax errors in this file. Fix them all to make the code run!

HINT: Start from the top and fix one error at a time. After fixing each error,
      run the code to see if there are more errors.
"""

# --- ERROR 1: Missing colon ---
# The error message will tell you there's a SyntaxError on line 21
# Look at the if statement - what's missing at the end?

x = 10
if x > 5
    print("x is greater than 5")

# --- ERROR 2: Missing closing parenthesis ---
# Look at the print statement - count the parentheses

print("The value of x is: " + str(x)

# --- ERROR 3: Missing closing bracket ---
# The list is missing something at the end

my_list = [1, 2, 3, 4, 5

# --- ERROR 4: Wrong indentation ---
# The print statement should be indented
# Remember: Python uses indentation to define code blocks

if x < 20:
print("x is less than 20")

# --- ERROR 5: Missing quotes ---
# The string is missing a closing quote

name = 'Alice
print("Hello, " + name)

# --- TEST YOUR CODE ---
# If you've fixed all the errors, the output should be:
# x is greater than 5
# The value of x is: 10
# [1, 2, 3, 4, 5]
# x is less than 20
# Hello, Alice

print("\nAll syntax errors fixed! ✅")
