# Exercise 6: Print Debugging
# ===========================

"""
In this exercise, you'll practice using print() statements for debugging.

Print debugging is one of the most effective techniques for finding logic errors.
By printing variable values at different points in your code, you can see exactly
what's happening and where things are going wrong.

Instructions:
1. Read the code and understand what it's supposed to do
2. Add print() statements to see what's happening
3. Run the code and look at the debug output
4. Identify where the logic is going wrong
5. Fix the code based on your findings

There are 3 functions with bugs. Use print debugging to find and fix them!

HINT: Add print statements BEFORE the error occurs to see what values
      your variables have. This will help you understand what's going wrong.
"""

# --- FUNCTION 1: find_max ---
# Expected: Return the maximum number in a list
# Current: Returns the minimum number

def find_max(numbers):
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num < max_num:  # Bug: Should be >
            max_num = num
    
    return max_num

print("Function 1: find_max")
print(f"find_max([3, 1, 4, 2]): {find_max([3, 1, 4, 2])}")  # Should be 4

# Your task:
# 1. Add print statements inside find_max to see what's happening
# 2. Run the code and look at the debug output
# 3. Identify the bug
# 4. Fix the code

# --- FUNCTION 2: count_vowels ---
# Expected: Count the number of vowels in a string
# Current: Counts consonants instead of vowels

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    
    for char in text.lower():
        if char not in vowels:  # Bug: Should be 'in' not 'not in'
            count += 1
    
    return count

print("\nFunction 2: count_vowels")
print(f"count_vowels('hello'): {count_vowels('hello')}")  # Should be 2 ('e', 'o')

# Your task:
# 1. Add print statements to see which characters are being counted
# 2. Run the code and look at the debug output
# 3. Identify the bug
# 4. Fix the code

# --- FUNCTION 3: calculate_discount ---
# Expected: Calculate the final price after applying a discount percentage
# Current: Returns the discount amount, not the final price

def calculate_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    return discount  # Bug: Should return price - discount

print("\nFunction 3: calculate_discount")
print(f"calculate_discount(100, 20): {calculate_discount(100, 20)}")  # Should be 80.0

# Your task:
# 1. Add print statements to see the discount and final calculation
# 2. Run the code and look at the debug output
# 3. Identify the bug
# 4. Fix the code

# --- TEST YOUR CODE ---
# After fixing all functions, the output should be:
# Function 1: find_max
# find_max([3, 1, 4, 2]): 4
# 
# Function 2: count_vowels
# count_vowels('hello'): 2
# 
# Function 3: calculate_discount
# calculate_discount(100, 20): 80.0
# 
# All print debugging exercises complete! ✅

print("\nAll print debugging exercises complete! ✅")
