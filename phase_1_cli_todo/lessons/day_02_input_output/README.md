# Day 2: User Input and Output

## 🎯 Learning Objectives

By the end of today, you will be able to:
- Use the `print()` function to display output
- Use the `input()` function to get user input
- Format strings using f-strings
- Use escape sequences for special characters
- Build simple interactive programs

---

## 📚 Lesson: The print() Function

The `print()` function is used to display output to the console (terminal).

### Basic Usage

```python
print("Hello, World!")  # Output: Hello, World!
print(42)              # Output: 42
print(True)            # Output: True
```

### Printing Multiple Items

You can pass multiple items to `print()`, separated by commas:

```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 25
```

**Note:** By default, `print()` adds a space between items and a newline at the end.

### Custom Separators

You can change the separator between items using the `sep` parameter:

```python
print("a", "b", "c")              # Output: a b c
print("a", "b", "c", sep="")     # Output: abc
print("a", "b", "c", sep="-")    # Output: a-b-c
print("a", "b", "c", sep="\n")   # Output: a (newline) b (newline) c
```

### Custom End Character

You can change what `print()` puts at the end using the `end` parameter:

```python
print("Hello", end="")      # Output: Hello (no newline)
print("World!")             # Output: World! (on same line)
# Combined output: HelloWorld!

print("Line 1", end=" ")   # Output: Line 1 (with space)
print("Line 2")             # Output: Line 2 (on same line)
# Combined output: Line 1 Line 2
```

---

## 📚 Lesson: The input() Function

The `input()` function is used to get input from the user. It always returns a **string**.

### Basic Usage

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**Example interaction:**
```
Enter your name: Alice
Hello, Alice!
```

### Important Note

**`input()` always returns a string!** Even if the user enters a number, it will be a string:

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'>, not <class 'int'>
```

If you need a number, you must convert it:

```python
age = int(input("Enter your age: "))
print(type(age))  # <class 'int'>
```

### Input with Type Conversion

```python
# Integer input
age = int(input("Enter your age: "))

# Float input
temperature = float(input("Enter temperature: "))

# Boolean input (accepts "True", "False", "1", "0", etc.)
is_valid = bool(input("Is this valid? (True/False): "))
```

**Warning:** If the user enters something that can't be converted, you'll get a `ValueError`. You'll learn how to handle this in later lessons.

---

## 📚 Lesson: String Formatting

There are several ways to format strings in Python. Let's look at the most common ones.

### 1. String Concatenation (Basic)

```python
name = "Alice"
age = 25
message = "Hello, " + name + "! You are " + str(age) + " years old."
print(message)
```

**Note:** You need to convert non-string values to strings using `str()`.

### 2. f-strings (Recommended - Python 3.6+)

**f-strings** are the most convenient and readable way to format strings:

```python
name = "Alice"
age = 25
message = f"Hello, {name}! You are {age} years old."
print(message)
```

**How it works:**
- Prefix the string with `f` (like `f"..."`)
- Put expressions inside `{}` braces
- The expressions are evaluated and inserted into the string

**Examples:**

```python
# Basic variable insertion
price = 19.99
print(f"Price: ${price}")  # Output: Price: $19.99

# Expressions inside braces
x = 10
y = 20
print(f"Sum: {x + y}")  # Output: Sum: 30

# Function calls inside braces
name = "alice"
print(f"Uppercase: {name.upper()}")  # Output: Uppercase: ALICE

# Formatting numbers
pi = 3.1415926535
print(f"Pi: {pi:.2f}")  # Output: Pi: 3.14 (2 decimal places)

# Zero-padding numbers
num = 7
print(f"Number: {num:03d}")  # Output: Number: 007 (3 digits with leading zeros)
```

**f-string formatting options:**

| Format | Meaning | Example |
|--------|---------|---------|
| `:d` | Decimal integer | `f"{42:d}"` → `"42"` |
| `:f` | Fixed-point float | `f"{3.14159:f}"` → `"3.141590"` |
| `:.2f` | Float with 2 decimals | `f"{3.14159:.2f}"` → `"3.14"` |
| `:e` | Scientific notation | `f"{1000:e}"` → `"1.000000e+03"` |
| `:s` | String | `f"{42:s}"` → `"42"` |
| `:05d` | Zero-padded integer | `f"{7:05d}"` → `"00007"` |

### 3. .format() Method (Older, but still useful)

```python
name = "Alice"
age = 25
message = "Hello, {}! You are {} years old.".format(name, age)
print(message)

# With named placeholders
message = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
print(message)
```

### 4. % Formatting (Old style - not recommended for new code)

```python
name = "Alice"
age = 25
message = "Hello, %s! You are %d years old." % (name, age)
print(message)
```

**Recommendation:** Use f-strings for new code. They're the most readable and powerful.

---

## 📚 Lesson: Escape Sequences

Sometimes you need to include special characters in strings. Escape sequences allow you to do this.

### Common Escape Sequences

| Escape Sequence | Meaning | Example |
|----------------|---------|---------|
| `\n` | Newline | `"Line 1\nLine 2"` → Two lines |
| `\t` | Tab | `"First\tSecond"` → First    Second |
| `\\` | Backslash | `"C:\\Users"` → C:\Users |
| `\'` | Single quote | `"It's raining"` → It's raining |
| `\"` | Double quote | `'He said "Hello"'` → He said "Hello" |
| `\r` | Carriage return | `"Hello\rWorld"` → World (overwrites) |
| `\b` | Backspace | `"Hello\b "` → Hell (removes last char) |

### Examples

```python
# Newline
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# Tab
print("First\tSecond")
# Output: First    Second

# Backslash
print("C:\Users\Name")
# Output: C:\Users\Name

# Single quote
print("It's a beautiful day!")
# Output: It's a beautiful day!

# Double quote
print('He said "Hello"')
# Output: He said "Hello"
```

### Raw Strings

If you have a lot of backslashes (like in file paths), use raw strings:

```python
# Normal string (need to escape backslashes)
path1 = "C:\\Users\\Name\\Documents"

# Raw string (backslashes are treated literally)
path2 = r"C:\Users\Name\Documents"

print(path1)  # C:\Users\Name\Documents
print(path2)  # C:\Users\Name\Documents
```

---

## 💡 Best Practices

### 1. User Prompts

Always include a prompt in `input()` to tell the user what to enter:

**Bad:**
```python
name = input()  # User doesn't know what to enter
```

**Good:**
```python
name = input("Enter your name: ")
```

### 2. Input Validation

Always validate user input. Don't assume the user will enter what you expect:

```python
# Bad: Assumes user enters a number
age = int(input("Enter your age: "))

# Better: Handle potential errors (you'll learn more about this later)
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")
```

### 3. Clear Output

Make your output easy to read:

**Bad:**
```python
print("Name:" + name + "Age:" + str(age))  # Output: Name:AliceAge:25
```

**Good:**
```python
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 25
# or
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 25
```

### 4. Consistent Formatting

Be consistent with your string formatting:

**Bad:**
```python
# Mixing different formatting styles
print("Name: " + name)
print(f"Age: {age}")
print("City: %s" % city)
```

**Good:**
```python
# Using f-strings consistently
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

---

## 🎯 Exercises

Now it's your turn! Complete the following exercises to practice what you've learned.

### Exercise Files

1. **exercise_1.py** - Basic input and output
2. **exercise_2.py** - String formatting and escape sequences

Open each file and follow the instructions inside.

---

## 📝 Knowledge Check

Test your understanding by answering these questions:

1. What does the `print()` function do?
   - Your answer: ________________________________________

2. What does the `input()` function do? What type does it always return?
   - Your answer: ________________________________________

3. How do you include a variable's value in a string using f-strings?
   - Your answer: ________________________________________

4. What is the difference between `print("a", "b")` and `print("a" + "b")`?
   - Your answer: ________________________________________

5. What escape sequence would you use to add a newline in a string?
   - Your answer: ________________________________________

6. What escape sequence would you use to add a tab in a string?
   - Your answer: ________________________________________

7. How would you format a float to display only 2 decimal places using f-strings?
   - Your answer: ________________________________________

---

## 🌟 Challenge (Optional)

Create a **Mad Libs** game that:
1. Asks the user for different types of words (noun, verb, adjective, etc.)
2. Stores each word in a variable
3. Inserts the words into a pre-written story template
4. Prints the completed story

Example:
```
Enter a noun: dog
Enter a verb: run
Enter an adjective: happy
Enter an adverb: quickly

The happy dog quickly run through the park.
```

**Hint:** Use f-strings or the `.format()` method to insert the words into the story.

---

## 📚 Additional Resources

- [Python Documentation - print()](https://docs.python.org/3/library/functions.html#print)
- [Python Documentation - input()](https://docs.python.org/3/library/functions.html#input)
- [Real Python - Python f-strings](https://realpython.com/f-strings/)
- [Python String Formatting Best Practices](https://pyformat.info/)
- [W3Schools - Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp)

---

## 🎉 Next Steps

Once you've completed the exercises:
1. Review your answers to the knowledge check
2. Try the optional challenge
3. Move on to **Day 3: Basic Operators**

**Great job on Day 2!** 🎉
