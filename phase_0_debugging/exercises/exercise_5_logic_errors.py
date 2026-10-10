# Exercise 5: Logic Errors
# ========================

"""
In this exercise, you'll practice identifying and fixing logic errors.

Logic errors are the trickiest because Python doesn't give you any error message!
Your code runs, but it produces the wrong result.

Instructions:
1. Look at what the code is supposed to do (read the comments)
2. Run the code and see what it actually does
3. Compare the expected output with the actual output
4. Use print() statements to see what's happening
5. Fix the logic to produce the correct result

There are 5 logic errors in this file. Fix them all!

HINT: Add print() statements to see variable values at different steps.
      Check edge cases (empty inputs, zero, etc.).
"""

# --- ERROR 1: Wrong calculation ---
# Expected: Calculate the average of a list of numbers
# Current: Returns the sum, not the average

def calculate_average(numbers):
    return sum(numbers)

result = calculate_average([1, 2, 3, 4, 5])
print(f"Average: {result}")  # Should be 3.0, not 15

# Fix: Divide the sum by the number of elements

# --- ERROR 2: Off-by-one in loop ---
# Expected: Print numbers 1 through 5
# Current: Prints 0 through 4

def print_numbers():
    for i in range(5):
        print(i)

print("\nNumbers 1-5:")
print_numbers()

# Fix: Adjust the range to start at 1

# --- ERROR 3: Incorrect condition ---
# Expected: Return True if number is even
# Current: Returns True if number is odd

def is_even(number):
    return number % 2 == 1

print(f"\nIs 4 even? {is_even(4)}")  # Should be True, currently False
print(f"Is 5 even? {is_even(5)}")  # Should be False, currently True

# Fix: Change the condition to check for evenness

# --- ERROR 4: Wrong index in list ---
# Expected: Get the last element of the list
# Current: Gets the first element

def get_last_element(lst):
    return lst[0]

my_list = [10, 20, 30, 40, 50]
print(f"\nLast element: {get_last_element(my_list)}")  # Should be 50, not 10

# Fix: Use the correct index for the last element

# --- ERROR 5: Accumulation error ---
# Expected: Sum all numbers in the list
# Current: Only returns the last number

def sum_list(numbers):
    total = 0
    for num in numbers:
        total = num  # Just assigns, doesn't accumulate
    return total

numbers = [5, 10, 15]
print(f"\nSum: {sum_list(numbers)}")  # Should be 30, currently 15

# Fix: Accumulate the numbers properly

# --- TEST YOUR CODE ---
# If you've fixed all the errors, the output should be:
# Average: 3.0
# Numbers 1-5:
# 1
# 2
# 3
# 4
# 5
# Is 4 even? True
# Is 5 even? False
# Last element: 50
# Sum: 30
# All logic errors fixed! ✅

print("\nAll logic errors fixed! ✅")
