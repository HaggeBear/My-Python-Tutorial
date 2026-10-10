# Common Python Errors: A Beginner's Guide

## 📚 Introduction

When you write Python code, you will encounter errors. **This is completely normal and expected!** Even experienced programmers see errors every day. The key is learning how to read and understand these error messages.

Python errors generally fall into two main categories:
1. **Syntax Errors** - Problems with the structure of your code
2. **Exceptions (Runtime Errors)** - Problems that occur while your code is running

Let's explore the most common errors you'll encounter as a beginner.

---

## 🔴 Syntax Errors

**Syntax errors** occur when Python doesn't understand the structure of your code. These are usually the easiest to fix because Python tells you exactly where the problem is.

### 1. SyntaxError

The most common syntax error. It means Python encountered code that violates its grammar rules.

**Example:**
```python
# Missing colon at the end of if statement
if x == 5
    print("x is 5")
```

**Error Message:**
```
  File "example.py", line 2
    if x == 5
            ^
SyntaxError: invalid syntax
```

**What Python is telling you:**
- The error is on line 2
- The problem is at the end of the line (the `^` points to where Python got confused)
- It's a syntax error (missing colon)

**How to fix:** Add the missing colon:
```python
if x == 5:
    print("x is 5")
```

### 2. IndentationError

Python uses indentation to define blocks of code. Incorrect indentation causes this error.

**Example:**
```python
if x > 0:
print("Positive")  # Missing indentation
```

**Error Message:**
```
  File "example.py", line 2
    print("Positive")
    ^
IndentationError: expected an indented block
```

**What Python is telling you:**
- Line 2 should be indented
- Python expected code to be indented after the `if` statement

**How to fix:** Add proper indentation (usually 4 spaces):
```python
if x > 0:
    print("Positive")
```

### 3. TabError

This occurs when you mix tabs and spaces for indentation.

**Example:**
```python
if x > 0:
    print("Positive")  # 4 spaces
	print("Still positive")  # Tab character
```

**Error Message:**
```
  File "example.py", line 3
    print("Still positive")
    ^
TabError: inconsistent use of tabs and spaces in indentation
```

**How to fix:**
- **Never mix tabs and spaces!**
- Configure your editor to use spaces only
- In VS Code: File > Preferences > Settings > Search "indent" > Set "Editor: Insert Spaces" to true

---

## 🟡 Runtime Errors (Exceptions)

**Runtime errors** occur when your code has correct syntax but something goes wrong while it's executing. These are also called **exceptions**.

### 1. NameError

This occurs when you try to use a variable or function that hasn't been defined.

**Example:**
```python
print(age)  # age has not been defined
```

**Error Message:**
```
  File "example.py", line 1, in <module>
    print(age)
NameError: name 'age' is not defined
```

**What Python is telling you:**
- The name `age` is not defined
- You're trying to use a variable that doesn't exist

**Common causes:**
- Misspelled variable name
- Forgot to define the variable
- Variable is out of scope

**How to fix:** Define the variable before using it:
```python
age = 25
print(age)
```

### 2. TypeError

This occurs when you try to perform an operation on incompatible types.

**Example:**
```python
x = "Hello"
y = 5
print(x + y)  # Can't add string and integer
```

**Error Message:**
```
  File "example.py", line 3, in <module>
    print(x + y)
TypeError: can only concatenate str (not "int") to str
```

**What Python is telling you:**
- You're trying to concatenate (add) a string and an integer
- Python can only add strings to other strings

**Common causes:**
- Mixing different types in operations
- Forgetting to convert types (e.g., string to integer)

**How to fix:** Convert types appropriately:
```python
x = "Hello"
y = 5
print(x + str(y))  # Convert y to string
```

### 3. IndexError

This occurs when you try to access an index that doesn't exist in a sequence (list, string, tuple).

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[5])  # There is no index 5
```

**Error Message:**
```
  File "example.py", line 2, in <module>
    print(fruits[5])
IndexError: list index out of range
```

**What Python is telling you:**
- You're trying to access index 5
- The list only has 3 items (indices 0, 1, 2)
- The index is "out of range"

**How to fix:**
- Check the length of the list first: `len(fruits)`
- Use a valid index:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[2])  # Last item
# or
print(fruits[-1])  # Also gets the last item
```

### 4. KeyError

This occurs when you try to access a dictionary key that doesn't exist.

**Example:**
```python
person = {"name": "Alice", "age": 30}
print(person["email"])  # 'email' key doesn't exist
```

**Error Message:**
```
  File "example.py", line 2, in <module>
    print(person["email"])
KeyError: 'email'
```

**What Python is telling you:**
- The key `'email'` doesn't exist in the dictionary

**How to fix:**
- Check if the key exists first:
```python
if "email" in person:
    print(person["email"])
else:
    print("Email not found")
```
- Or use the `.get()` method which returns `None` if key doesn't exist:
```python
print(person.get("email", "Email not found"))
```

### 5. ValueError

This occurs when a function receives an argument of the correct type but an inappropriate value.

**Example:**
```python
number = int("abc")  # Can't convert "abc" to integer
```

**Error Message:**
```
  File "example.py", line 1, in <module>
    number = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

**What Python is telling you:**
- You're trying to convert "abc" to an integer
- "abc" is not a valid integer

**Common causes:**
- Trying to convert non-numeric strings to numbers
- Unpacking iterables with wrong number of values

**How to fix:**
- Validate input first:
```python
text = "abc"
if text.isdigit():
    number = int(text)
else:
    print("Not a valid number")
```

### 6. AttributeError

This occurs when you try to access an attribute or method that doesn't exist for an object.

**Example:**
```python
x = 10
x.append(5)  # Integers don't have an append method
```

**Error Message:**
```
  File "example.py", line 2, in <module>
    x.append(5)
AttributeError: 'int' object has no attribute 'append'
```

**What Python is telling you:**
- You're trying to use `.append()` on an integer
- Integers don't have an `append` method

**Common causes:**
- Using the wrong method for a type
- Misspelled method name
- Variable is the wrong type

**How to fix:** Use the correct method for the type:
```python
# If you want to append to a list:
lst = [10]
lst.append(5)
```

### 7. ZeroDivisionError

This occurs when you try to divide by zero.

**Example:**
```python
x = 10 / 0
```

**Error Message:**
```
  File "example.py", line 1, in <module>
    x = 10 / 0
ZeroDivisionError: division by zero
```

**How to fix:** Always check for zero before dividing:
```python
denominator = 0
if denominator != 0:
    x = 10 / denominator
else:
    print("Cannot divide by zero")
```

---

## 🟢 Logic Errors

**Logic errors** are the trickiest because Python doesn't give you any error message. Your code runs, but it produces the wrong result.

**Example:**
```python
# Calculate the average of a list
def average(numbers):
    return sum(numbers)  # Forgot to divide by len(numbers)

result = average([1, 2, 3, 4, 5])
print(result)  # Outputs 15, but should be 3
```

**Why it's hard:**
- No error message
- Code runs without crashing
- But the result is wrong

**How to find logic errors:**
1. **Add print statements** to see what's happening:
   ```python
   def average(numbers):
       total = sum(numbers)
       print(f"DEBUG: total = {total}, count = {len(numbers)}")
       return total / len(numbers)
   ```

2. **Check edge cases:**
   - Empty list
   - Single item list
   - Negative numbers
   - Very large numbers

3. **Manual calculation:**
   - Calculate the expected result by hand
   - Compare with what your code produces

4. **Rubber duck debugging:**
   - Explain your code line by line to a rubber duck (or a friend)
   - Often you'll find the bug while explaining

---

## 📖 Reading Tracebacks

A **traceback** is Python's way of showing you where an error occurred. Learning to read tracebacks is crucial for debugging.

**Example Traceback:**
```
Traceback (most recent call last):
  File "my_program.py", line 10, in <module>
    result = calculate_total(items)
  File "my_program.py", line 5, in calculate_total
    return sum(item['price'] for item in items)
  File "my_program.py", line 5, in <genexpr>
    sum(item['price'] for item in items)
KeyError: 'price'
```

**How to read this:**

1. **Start from the bottom** - The actual error is at the end:
   - `KeyError: 'price'` - This is the error type and message

2. **Look at the middle** - This shows the call stack:
   - Line 5 in `calculate_total` function
   - Specifically in the generator expression: `sum(item['price'] for item in items)`

3. **Look at the top** - This shows where the error originated:
   - Line 10 in the main module
   - The call to `calculate_total(items)`

4. **Put it together:**
   - The error is a `KeyError` for the key `'price'`
   - It happened when trying to access `item['price']` in the generator
   - This was called from line 10
   - The issue: One of the items in the `items` list doesn't have a `'price'` key

---

## 🎯 Debugging Strategies

### 1. The Print Statement Method

The simplest and most effective debugging technique for beginners.

**How to use:**
```python
def calculate_discount(price, discount_percent):
    print(f"DEBUG: price={price}, discount_percent={discount_percent}")
    discount_amount = price * discount_percent
    print(f"DEBUG: discount_amount={discount_amount}")
    final_price = price - discount_amount
    print(f"DEBUG: final_price={final_price}")
    return final_price
```

**When to use:**
- When you want to see the values of variables
- When you want to trace the flow of execution
- When you're not sure if a block of code is being executed

### 2. The Comment Out Method

If you're not sure which part of your code is causing the problem, try commenting out sections.

**How to use:**
```python
# Original code (has an error)
def process_data(data):
    result = data * 2
    result = result + 10
    result = result / 0  # This line causes ZeroDivisionError
    return result

# Comment out suspicious lines
def process_data(data):
    result = data * 2
    # result = result + 10
    # result = result / 0
    return result
```

### 3. The Divide and Conquer Method

Break your code into smaller pieces and test each piece independently.

**How to use:**
```python
# Instead of testing the whole function at once
def complex_operation(data):
    # Step 1: Process data
    processed = data.upper()
    
    # Step 2: Filter data
    filtered = [x for x in processed if x.isalpha()]
    
    # Step 3: Calculate result
    result = len(filtered) * 2
    
    return result

# Test each step separately
print(data.upper())  # Test step 1
print([x for x in data.upper() if x.isalpha()])  # Test step 2
print(len([x for x in data.upper() if x.isalpha()]) * 2)  # Test step 3
```

---

## 🛡️ Defensive Programming

**Prevent errors before they happen** by writing defensive code:

### 1. Input Validation
```python
def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 2. Use .get() for Dictionaries
```python
# Instead of:
value = my_dict['key']  # Raises KeyError if 'key' doesn't exist

# Use:
value = my_dict.get('key', default_value)
```

### 3. Check List Lengths
```python
if len(my_list) > 0:
    first_item = my_list[0]
else:
    first_item = None
```

### 4. Try/Except Blocks
```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error occurred: {e}")
    result = default_value
except Exception as e:
    print(f"Unexpected error: {e}")
    result = None
```

---

## 📝 Quick Reference Table

| Error Type | Cause | Example | Fix |
|------------|-------|---------|-----|
| SyntaxError | Invalid Python syntax | Missing colon, wrong indentation | Check line indicated in error |
| IndentationError | Incorrect indentation | Mixing tabs and spaces | Use consistent indentation |
| NameError | Undefined variable | Using variable before definition | Define variable first |
| TypeError | Invalid operation for type | Adding string + integer | Convert types or use appropriate operations |
| IndexError | Index out of range | Accessing list[10] when len=5 | Check length first, use valid indices |
| KeyError | Dictionary key doesn't exist | Accessing dict['missing'] | Use .get() or check if key exists |
| ValueError | Invalid value for operation | int("abc") | Validate input first |
| AttributeError | Object has no attribute | "hello".append("!") | Use correct methods for the type |
| ZeroDivisionError | Division by zero | 10 / 0 | Check for zero before dividing |

---

## 🎉 Practice Time!

Now that you understand common errors, it's time to practice!

**Next Step:** Open `exercises/exercise_1_syntax_errors.py` and start fixing the broken code!

Remember:
1. Read the error message carefully
2. Identify the error type
3. Look at the line number
4. Think about what's wrong
5. Fix the code

You've got this! 💪
