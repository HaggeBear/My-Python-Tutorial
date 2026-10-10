# Exercise 4: Index Errors
# =========================

"""
In this exercise, you'll practice identifying and fixing IndexError.

An IndexError occurs when you try to access an index that doesn't exist
in a sequence (list, string, tuple, etc.).

Remember: Python uses 0-based indexing!
- First element: index 0
- Second element: index 1
- Last element: index -1 or len(list) - 1

Instructions:
1. Read the error message carefully
2. Identify which index is causing the problem
3. Check the length of the sequence
4. Fix the error by using a valid index
5. Run the code to verify it works

There are 5 IndexErrors in this file. Fix them all!

HINT: Use len() to check the length of sequences.
      Use print() to see what indices are valid.
"""

# --- ERROR 1: Accessing beyond list length ---
# The list has 3 elements (indices 0, 1, 2)

fruits = ["apple", "banana", "cherry"]
print(fruits[3])  # IndexError: list index out of range

# Fix: Use a valid index (0, 1, or 2)

# --- ERROR 2: Negative index out of range ---
# Negative indices count from the end, but -4 is too far

colors = ["red", "green", "blue"]
print(colors[-4])  # IndexError: list index out of range

# Fix: Use a valid negative index (-1, -2, or -3)

# --- ERROR 3: String index out of range ---
# Strings are also sequences and can have IndexError

word = "hello"
print(word[10])  # IndexError: string index out of range

# Fix: Use a valid index (0 to 4)

# --- ERROR 4: Empty list ---
# Can't access any index of an empty list

empty_list = []
print(empty_list[0])  # IndexError: list index out of range

# Fix: Check if list is empty first

# --- ERROR 5: Loop with wrong range ---
# The loop goes one too far

numbers = [10, 20, 30]
for i in range(4):  # Will try to access index 3
    print(numbers[i])

# Fix: Use range(len(numbers)) instead

# --- TEST YOUR CODE ---
# If you've fixed all the errors, the output should be:
# cherry (or whatever fruit you chose at index 2)
# blue (or whatever color you chose)
# o (or whatever character you chose)
# (nothing for empty list, or your message)
# 10, 20, 30 (each on a new line)
# All index errors fixed! ✅

print("\nAll index errors fixed! ✅")
