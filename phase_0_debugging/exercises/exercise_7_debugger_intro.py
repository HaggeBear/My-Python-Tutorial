# Exercise 7: Debugger Introduction
# ================================

"""
In this exercise, you'll learn to use Python's built-in debugger (pdb).

The debugger allows you to:
- Pause your code at specific points (breakpoints)
- Step through your code line by line
- Inspect variable values
- Understand the flow of execution

Instructions:
1. Add a breakpoint using pdb.set_trace()
2. Run the code
3. When the debugger pauses, use commands to step through the code
4. Inspect variables to understand what's happening
5. Fix the bugs you find

HINT: pdb commands:
- n (next): Execute next line
- s (step): Step into function
- c (continue): Continue to next breakpoint
- p <var> (print): Print variable value
- l (list): Show code around current line
- q (quit): Quit debugger
"""

import pdb

# --- PART 1: Using pdb.set_trace() ---
# Add a breakpoint and use the debugger to find the bug

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = num  # Bug: Should be total += num
    return total

result = calculate_sum([1, 2, 3, 4, 5])
print(f"Sum: {result}")  # Should be 15, currently 5

# Your task:
# 1. Add pdb.set_trace() at the beginning of calculate_sum
# 2. Run the code
# 3. When debugger pauses, use 'n' to step through
# 4. Use 'p total' and 'p num' to see values
# 5. Identify the bug
# 6. Fix the code

# --- PART 2: Debugging with breakpoints ---
# Set a breakpoint to catch the error early

def process_data(data):
    processed = []
    for item in data:
        # Bug: Should append item * 2, not item
        processed.append(item)
    return processed

result = process_data([1, 2, 3])
print(f"\nProcessed data: {result}")  # Should be [2, 4, 6]

# Your task:
# 1. Add pdb.set_trace() before the for loop
# 2. Run the code
# 3. Use 'p item' to see what's being appended
# 4. Identify the bug
# 5. Fix the code

# --- PART 3: Using the debugger to understand flow ---
# Use the debugger to understand why this function returns the wrong result

def find_duplicates(items):
    duplicates = []
    for item in items:
        if items.count(item) > 1:
            duplicates.append(item)
    # Bug: Returns duplicates with duplicates (e.g., [2, 2, 3, 3])
    return duplicates

result = find_duplicates([1, 2, 2, 3, 3, 3, 4])
print(f"\nDuplicates: {result}")  # Should be [2, 3] without duplicates

# Your task:
# 1. Add pdb.set_trace() at the beginning of find_duplicates
# 2. Run the code
# 3. Step through and watch what gets appended
# 4. Identify the bug
# 5. Fix the code to return unique duplicates only

# --- TEST YOUR CODE ---
# After fixing all functions, the output should be:
# Sum: 15
# Processed data: [2, 4, 6]
# Duplicates: [2, 3]
# 
# All debugger exercises complete! ✅

print("\nAll debugger exercises complete! ✅")
