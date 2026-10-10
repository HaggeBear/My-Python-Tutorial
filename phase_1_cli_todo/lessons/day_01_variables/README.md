# Day 1: Variables and Data Types

## 🎯 Learning Objectives

By the end of today, you will be able to:
- Understand what variables are and why they're used
- Create variables in Python
- Understand different data types (integers, floats, strings, booleans)
- Use the `type()` function to check variable types
- Follow Python naming conventions (PEP 8)
- Convert between different data types

---

## 📚 Lesson: Variables

### What is a Variable?

A **variable** is like a box in your computer's memory that stores a value. You give it a name so you can refer to that value later.

Think of variables like labeled jars in a kitchen:
- You have a jar labeled "sugar" that contains sugar
- You have a jar labeled "flour" that contains flour
- When you need sugar, you look for the jar labeled "sugar"

In Python:
- The **variable name** is like the label on the jar
- The **value** is what's inside the jar

### Creating Variables

In Python, you create a variable by giving it a name and assigning it a value:

```python
# Variable name = value
age = 25
name = "Alice"
height = 5.9
```

The `=` symbol is called the **assignment operator**. It assigns the value on the right to the variable name on the left.

### Variable Naming Rules

1. **Must start with a letter or underscore (_)**
   - ✅ `name`, `_private`, `age1`
   - ❌ `1age`, `@name`

2. **Can contain letters, numbers, and underscores**
   - ✅ `user_name`, `total2`, `first_name`
   - ❌ `user-name`, `total@amount`

3. **Cannot be a Python keyword**
   - ❌ `if = 10`, `for = 5`, `def = "test"`
   - Python keywords: `if`, `else`, `for`, `while`, `def`, `return`, etc.

4. **Case-sensitive**
   - `age`, `Age`, and `AGE` are three different variables

### Python Naming Conventions (PEP 8)

PEP 8 is Python's official style guide. Following these conventions makes your code more readable:

1. **Variable names should be lowercase**
   - ✅ `user_name`, `total_amount`
   - ❌ `UserName`, `TOTAL_AMOUNT`

2. **Use underscores to separate words (snake_case)**
   - ✅ `user_name`, `first_name`, `last_name`
   - ❌ `userName`, `firstname`

3. **Make names descriptive and meaningful**
   - ✅ `number_of_students`, `user_age`
   - ❌ `x`, `n`, `temp` (unless in very short, obvious contexts)

4. **Constants (values that never change) should be UPPERCASE**
   - ✅ `MAX_SPEED = 100`, `PI = 3.14159`
   - ❌ `max_speed = 100`

---

## 📚 Lesson: Data Types

Python has several built-in data types. Let's look at the most common ones:

### 1. Integers (`int`)

**Whole numbers** (positive, negative, or zero)

```python
age = 25
count = -10
temperature = 0
```

**Characteristics:**
- No decimal point
- Can be positive or negative
- Unlimited size (in Python 3)

### 2. Floating-Point Numbers (`float`)

**Numbers with a decimal point**

```python
height = 5.9
price = 19.99
temperature = -3.5
```

**Characteristics:**
- Has a decimal point
- Can be positive or negative
- Can represent very large or very small numbers using scientific notation

**Scientific Notation:**
```python
big_number = 1e6   # 1,000,000 (1 million)
small_number = 1e-3  # 0.001
```

### 3. Strings (`str`)

**Text data** - anything enclosed in quotes

```python
name = "Alice"
greeting = 'Hello, World!'
message = "It's a beautiful day!"  # Use double quotes for strings with apostrophes
```

**Characteristics:**
- Enclosed in single (`'`) or double (`"`) quotes
- Can contain letters, numbers, symbols, spaces
- Immutable (cannot be changed after creation)

**Multi-line strings:**
```python
# Using triple quotes
poem = """
Roses are red
Violets are blue
Sugar is sweet
And so are you
"""
```

### 4. Booleans (`bool`)

**Represents truth values** - either `True` or `False`

```python
is_raining = True
has_permission = False
is_valid = True
```

**Characteristics:**
- Only two possible values: `True` or `False`
- Note the capitalization (True/False, not true/false)
- Often used in conditional statements

---

## 🔍 The `type()` Function

You can check the type of any variable using the `type()` function:

```python
age = 25
print(type(age))        # <class 'int'>

height = 5.9
print(type(height))     # <class 'float'>

name = "Alice"
print(type(name))       # <class 'str'>

is_valid = True
print(type(is_valid))   # <class 'bool'>
```

---

## 🔄 Type Conversion

Sometimes you need to convert one type to another. Python provides several functions for this:

### Common Conversion Functions

| Function | Converts | Example |
|----------|----------|---------|
| `int()` | To integer | `int("5")` → `5` |
| `float()` | To float | `float("3.14")` → `3.14` |
| `str()` | To string | `str(42)` → `"42"` |
| `bool()` | To boolean | `bool(1)` → `True` |

### Examples

```python
# String to integer
age_str = "25"
age = int(age_str)
print(type(age))  # <class 'int'>

# Integer to string
count = 10
count_str = str(count)
print(type(count_str))  # <class 'str'>

# Float to integer (truncates decimal)
price = 19.99
price_int = int(price)
print(price_int)  # 19

# Integer to float
num = 5
num_float = float(num)
print(num_float)  # 5.0

# To boolean
# Empty values (0, "", [], etc.) become False
# Non-empty values become True
print(bool(0))     # False
print(bool(""))    # False
print(bool(1))     # True
print(bool("hi"))  # True
```

### Automatic Type Conversion

Python sometimes converts types automatically:

```python
# Integer + Float = Float
result = 5 + 3.14
print(result)  # 8.14
print(type(result))  # <class 'float'>

# Integer + Integer = Integer
result = 5 + 3
print(result)  # 8
print(type(result))  # <class 'int'>
```

**Note:** Python does NOT automatically convert between strings and numbers:
```python
# This will cause a TypeError
result = "5" + 3  # TypeError: can only concatenate str (not "int") to str

# You need to convert explicitly
result = int("5") + 3  # 8
```

---

## 💡 Best Practices

### 1. Choose Descriptive Names

**Bad:**
```python
x = 10
y = 20
z = x + y
```

**Good:**
```python
width = 10
height = 20
area = width * height
```

### 2. Use Consistent Naming

**Bad:**
```python
userName = "Alice"
user_age = 30
UserAddress = "123 Main St"
```

**Good:**
```python
user_name = "Alice"
user_age = 30
user_address = "123 Main St"
```

### 3. Initialize Variables Before Use

Always give a variable a value before using it:

**Bad:**
```python
print(total)  # NameError: name 'total' is not defined
total = 10
```

**Good:**
```python
total = 10
print(total)
```

### 4. One Variable = One Purpose

Avoid reusing variables for different purposes:

**Bad:**
```python
result = 10 + 5
print(result)
result = "Hello"  # Reusing result for a different purpose
print(result)
```

**Good:**
```python
sum_result = 10 + 5
print(sum_result)
greeting = "Hello"
print(greeting)
```

---

## 🎯 Exercises

Now it's your turn! Complete the following exercises to practice what you've learned.

### Exercise Files

1. **exercise_1.py** - Variable creation and naming
2. **exercise_2.py** - Data types and type conversion

Open each file and follow the instructions inside.

---

## 📝 Knowledge Check

Test your understanding by answering these questions:

1. What is a variable in Python?
   - Your answer: ________________________________________

2. What are the four main data types we learned today?
   - Your answer: ________________________________________

3. How do you check the type of a variable?
   - Your answer: ________________________________________

4. What is the difference between `int` and `float`?
   - Your answer: ________________________________________

5. How do you convert a string to an integer?
   - Your answer: ________________________________________

6. What are the variable naming rules in Python?
   - Your answer: ________________________________________

7. What is PEP 8 and why is it important?
   - Your answer: ________________________________________

---

## 🌟 Challenge (Optional)

Create a program that:
1. Asks the user for their name, age, and height
2. Stores each piece of information in a separate variable
3. Prints out a sentence using all three variables

Example output:
```
Please enter your name: Alice
Please enter your age: 25
Please enter your height (in meters): 1.75

Hello Alice! You are 25 years old and 1.75 meters tall.
```

---

## 📚 Additional Resources

- [Python Documentation - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 - Python Style Guide](https://peps.python.org/pep-0008/)
- [Real Python - Variables in Python](https://realpython.com/python-variables/)
- [W3Schools - Python Variables](https://www.w3schools.com/python/python_variables.asp)

---

## 🎉 Next Steps

Once you've completed the exercises:
1. Review your answers to the knowledge check
2. Try the optional challenge
3. Move on to **Day 2: User Input and Output**

**Great job on Day 1!** 🎉
