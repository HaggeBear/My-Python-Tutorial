# Debugging Cheat Sheet 📋

## 🚀 Quick Start Guide

Stuck on an error? Follow these steps:

```
1. ✅ DON'T PANIC - Errors are normal!
2. ✅ READ the error message carefully
3. ✅ LOOK at the line number mentioned
4. ✅ THINK about what the code is trying to do
5. ✅ CHECK your assumptions (variable values, types, etc.)
6. ✅ TRY a fix and test again
```

---

## 🔍 Error Message Breakdown

### Python Traceback Structure

```
Traceback (most recent call last):
  File "your_file.py", line 10, in <module>
    result = my_function(data)
  File "your_file.py", line 5, in my_function
    return data['key']
KeyError: 'key'
```

**How to read it:**
1. **Start at the bottom** → `KeyError: 'key'` (the actual error)
2. **Middle** → Line 5 in `my_function` (where it happened)
3. **Top** → Line 10 in main (where it was called from)

---

## 🎯 Common Errors & Fixes

### Syntax Errors

| Error | Example | Fix |
|-------|---------|-----|
| Missing `:` | `if x == 5` | Add colon: `if x == 5:` |
| Missing `)` | `print("Hello"` | Add parenthesis: `print("Hello")` |
| Missing `]` | `my_list = [1, 2, 3` | Add bracket: `my_list = [1, 2, 3]` |
| Missing `"` | `name = 'Alice` | Add quote: `name = 'Alice'` |
| Wrong indentation | `if x>0:` then `print(x)` without indent | Indent: `if x>0:` then `    print(x)` |

### Runtime Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError` | Variable not defined | Define the variable first |
| `TypeError` | Wrong type for operation | Convert types: `int("5")`, `str(10)` |
| `IndexError` | List index out of range | Check `len()` first, use valid index |
| `KeyError` | Dictionary key missing | Use `.get()` or check `if key in dict` |
| `ValueError` | Invalid value | Validate input: `if text.isdigit()` |
| `AttributeError` | Method doesn't exist | Use correct method for the type |
| `ZeroDivisionError` | Division by zero | Check `if denominator != 0` |

---

## 🐞 Debugging Techniques

### 1. Print Debugging (Easiest!)

**Add print statements to see what's happening:**

```python
# Before
result = calculate_something(data)

# After - Add debug prints
def calculate_something(data):
    print(f"DEBUG: Input data = {data}")  # See input
    
    intermediate = data * 2
    print(f"DEBUG: intermediate = {intermediate}")  # See calculation
    
    if intermediate > 10:
        print("DEBUG: Entered if block")  # Confirm block executes
        result = intermediate + 5
    else:
        print("DEBUG: Entered else block")
        result = intermediate - 5
    
    print(f"DEBUG: Final result = {result}")  # See output
    return result
```

**Pro Tip:** Use descriptive messages so you know what each print is showing.

---

### 2. Type Checking

**Check variable types when you get TypeError:**

```python
print(f"Type of x: {type(x)}")
print(f"Type of y: {type(y)}")

# For collections
print(f"Length of list: {len(my_list)}")
print(f"Keys in dict: {list(my_dict.keys())}")
```

---

### 3. The `dir()` Function

**See what methods an object has:**

```python
my_string = "Hello"
print(dir(my_string))  # Shows all string methods

my_list = [1, 2, 3]
print(dir(my_list))  # Shows all list methods
```

---

### 4. Using `help()`

**Get documentation for functions:**

```python
help(print)       # Shows print function documentation
help(str.split)   # Shows string split method documentation
help(list.append) # Shows list append method documentation
```

---

### 5. The Python Debugger (pdb)

**Step-by-step debugging:**

```python
import pdb

# Set a breakpoint
def my_function(data):
    pdb.set_trace()  # Execution will pause here
    result = data * 2
    return result

# Or run from command line
# $ python -m pdb your_script.py
```

**pdb Commands:**

| Command | Shortcut | What it does |
|---------|----------|--------------|
| `next` | `n` | Execute next line (step over functions) |
| `step` | `s` | Step into function |
| `continue` | `c` | Continue execution until next breakpoint |
| `quit` | `q` | Quit debugger |
| `print <var>` | `p <var>` | Print variable value |
| `list` | `l` | Show code around current line |
| `where` | `w` | Show stack trace |
| `break <line>` | `b <line>` | Set breakpoint at line |

---

### 6. VS Code Debugger (Recommended!)

**Setup:**
1. Open your Python file in VS Code
2. Click the Run and Debug icon (or press Ctrl+Shift+D)
3. Click "Run and Debug" or press F5
4. VS Code will automatically create a launch configuration

**Debugger Features:**
- Set breakpoints by clicking next to line numbers
- Step through code with toolbar buttons
- Inspect variables in the Variables panel
- Watch expressions in the Watch panel
- See the call stack

**Keyboard Shortcuts:**
- F5: Start/Continue
- F10: Step Over
- F11: Step Into
- Shift+F11: Step Out
- Ctrl+Shift+F5: Restart
- Shift+F5: Stop

---

## 🧩 Debugging Checklist

When you encounter an error, go through this checklist:

### For Syntax Errors
- [ ] Is there a missing `:` at the end of if/for/while/def?
- [ ] Are all parentheses `()` balanced?
- [ ] Are all brackets `[]` balanced?
- [ ] Are all braces `{}` balanced?
- [ ] Are all quotes `""` or `''` balanced?
- [ ] Is indentation consistent (all spaces or all tabs)?
- [ ] Are there any typos in keywords (if, for, while, def, etc.)?

### For NameError
- [ ] Is the variable defined before use?
- [ ] Is the variable name spelled correctly?
- [ ] Is the variable in scope?
- [ ] Did you forget to import a module?

### For TypeError
- [ ] Are you mixing incompatible types?
- [ ] Do you need to convert a type? (int(), str(), float(), etc.)
- [ ] Are you using the correct operation for the type?

### For IndexError
- [ ] Is the index within the valid range?
- [ ] Did you check the length first?
- [ ] Are you using 0-based indexing?
- [ ] Could the list be empty?

### For KeyError
- [ ] Does the key exist in the dictionary?
- [ ] Did you check with `if key in dict`?
- [ ] Could you use `.get()` with a default value?

### For Logic Errors (No Error Message)
- [ ] Add print statements to see variable values
- [ ] Check edge cases (empty list, zero, None, etc.)
- [ ] Test with simple, known inputs
- [ ] Compare your output with expected output
- [ ] Try rubber duck debugging (explain code line by line)

---

## 💡 Common Beginner Mistakes

### 1. Off-by-One Errors
```python
# Wrong: Python uses 0-based indexing
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4 (not 1-5)

# Right: If you want 1-5
for i in range(1, 6):
    print(i)  # Prints 1, 2, 3, 4, 5
```

### 2. Modifying Lists While Iterating
```python
# Wrong: Modifying list while iterating causes issues
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # This will skip elements!

# Right: Create a new list
numbers = [1, 2, 3, 4, 5]
evens = [num for num in numbers if num % 2 == 0]
```

### 3. Mutable Default Arguments
```python
# Wrong: Default list is created once when function is defined
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# Right: Use None as default
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

### 4. Integer Division
```python
# Python 3: / always returns float, // for integer division
result = 5 / 2   # Returns 2.5 (float)
result = 5 // 2  # Returns 2 (integer)
```

### 5. String Immutability
```python
# Wrong: Strings are immutable
my_string = "Hello"
my_string[0] = "J"  # TypeError: 'str' object does not support item assignment

# Right: Create a new string
my_string = "Hello"
my_string = "J" + my_string[1:]  # "Jello"
```

---

## 🎯 Debugging Mindset Tips

### 1. The Error is in YOUR Code
- The computer is always right
- If there's a bug, it's in your code, not Python
- Don't blame the language or tools

### 2. Small Changes
- Fix one thing at a time
- Test after each change
- Don't make multiple changes at once

### 3. Isolate the Problem
- Comment out code to narrow down the issue
- Create a minimal example that reproduces the error
- Remove unrelated code

### 4. Take Breaks
- If you're stuck, take a walk
- Come back with fresh eyes
- Often the solution will be obvious

### 5. Rubber Duck Debugging
- Explain your code line by line to a rubber duck
- Or to a friend, or even to yourself
- The act of explaining often reveals the bug

### 6. Search Online
- Copy and paste the error message into Google
- Add "Python" to your search
- Stack Overflow is your friend!

---

## 📚 Quick Reference Commands

| Task | Command |
|------|---------|
| Check Python version | `python --version` or `python3 --version` |
| Run a Python file | `python filename.py` |
| Run Python interactively | `python` or `python3` |
| Install a package | `pip install package_name` |
| Check installed packages | `pip list` |
| Run debugger | `python -m pdb script.py` |
| Check syntax without running | `python -m py_compile script.py` |

---

## 🎉 Remember!

```
✅ Every error is a learning opportunity
✅ Debugging is a skill that improves with practice
✅ The more errors you fix, the better you get
✅ Even expert programmers debug every day
✅ You CAN figure this out!
```

**Keep this cheat sheet handy as you work through the exercises!**
