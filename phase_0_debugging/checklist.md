# Phase 0: Debugging Checklist

## 🎯 Phase Completion Checklist

Before moving to Phase 1, make sure you can do all of the following. Check off each item as you complete it.

---

## ✅ Understanding Error Messages

- [ ] I can read a Python traceback and identify the error type
- [ ] I understand the difference between SyntaxError and runtime errors
- [ ] I can identify which line of code is causing an error from the traceback
- [ ] I understand what the `^` symbol points to in error messages

---

## ✅ Syntax Errors

- [ ] I can fix missing colons (`:`) in if/for/while/def statements
- [ ] I can fix missing parentheses `()` in function calls and expressions
- [ ] I can fix missing brackets `[]` in lists
- [ ] I can fix missing braces `{}` in dictionaries and sets
- [ ] I can fix missing quotes in strings
- [ ] I can fix indentation errors (using consistent spaces)
- [ ] I understand why mixing tabs and spaces causes problems

**Practice:** Complete `exercises/exercise_1_syntax_errors.py`

---

## ✅ NameError

- [ ] I understand that NameError means a variable is not defined
- [ ] I can fix NameError by defining variables before use
- [ ] I can spot and fix misspelled variable names
- [ ] I understand variable scope (variables inside functions are local)
- [ ] I know to import modules before using them

**Practice:** Complete `exercises/exercise_2_name_errors.py`

---

## ✅ TypeError

- [ ] I understand that TypeError means incompatible types for an operation
- [ ] I can fix TypeError by converting types (int(), str(), float(), etc.)
- [ ] I know common operations that cause TypeError (adding string + int, etc.)
- [ ] I can use type() to check variable types
- [ ] I understand that different types have different methods

**Practice:** Complete `exercises/exercise_3_type_errors.py`

---

## ✅ IndexError

- [ ] I understand that IndexError means an index is out of range
- [ ] I know Python uses 0-based indexing
- [ ] I can use len() to check the length of a sequence
- [ ] I understand negative indices (e.g., -1 for last element)
- [ ] I can fix IndexError by checking lengths and using valid indices
- [ ] I understand that strings can also have IndexError

**Practice:** Complete `exercises/exercise_4_index_errors.py`

---

## ✅ Logic Errors

- [ ] I understand that logic errors don't produce error messages
- [ ] I know that logic errors produce wrong results instead of crashing
- [ ] I can identify logic errors by comparing expected vs. actual output
- [ ] I can use print() statements to trace variable values
- [ ] I can test edge cases (empty inputs, zero, None, etc.)

**Practice:** Complete `exercises/exercise_5_logic_errors.py`

---

## ✅ Print Debugging

- [ ] I can add print() statements to see variable values
- [ ] I can use print() to trace the flow of execution
- [ ] I can use formatted strings (f-strings) for clear debug output
- [ ] I know to add descriptive messages to print statements
- [ ] I can use print() to check if a block of code is being executed

**Practice:** Complete `exercises/exercise_6_print_debugging.py`

---

## ✅ Using the Debugger (pdb)

- [ ] I can add breakpoints using pdb.set_trace()
- [ ] I can run code with the debugger: `python -m pdb script.py`
- [ ] I know the basic pdb commands:
    - [ ] `n` or `next`: Execute next line
    - [ ] `s` or `step`: Step into function
    - [ ] `c` or `continue`: Continue to next breakpoint
    - [ ] `p <var>` or `print <var>`: Print variable value
    - [ ] `l` or `list`: Show code around current line
    - [ ] `w` or `where`: Show stack trace
    - [ ] `q` or `quit`: Quit debugger
    - [ ] `b <line>` or `break <line>`: Set breakpoint
- [ ] I can step through code line by line
- [ ] I can inspect variable values in the debugger

**Practice:** Complete `exercises/exercise_7_debugger_intro.py`

---

## ✅ VS Code Debugger

- [ ] I have VS Code installed
- [ ] I can open a Python file in VS Code
- [ ] I can set breakpoints by clicking next to line numbers
- [ ] I can start debugging with F5 or the Run > Start Debugging menu
- [ ] I can use the debug toolbar:
    - [ ] Continue (F5)
    - [ ] Step Over (F10)
    - [ ] Step Into (F11)
    - [ ] Step Out (Shift+F11)
    - [ ] Restart (Ctrl+Shift+F5)
    - [ ] Stop (Shift+F5)
- [ ] I can inspect variables in the Variables panel
- [ ] I can add expressions to the Watch panel
- [ ] I can see the call stack

---

## ✅ Defensive Programming

- [ ] I understand the importance of input validation
- [ ] I can check if a key exists in a dictionary before accessing it
- [ ] I can check if a list is empty before accessing elements
- [ ] I can use .get() with default values for dictionaries
- [ ] I can use try/except blocks to handle errors gracefully

---

## ✅ Debugging Mindset

- [ ] I don't panic when I see errors
- [ ] I read error messages carefully
- [ ] I start debugging from the bottom of the traceback
- [ ] I make small changes and test frequently
- [ ] I use rubber duck debugging (explain code out loud)
- [ ] I take breaks when I'm stuck
- [ ] I search online for error messages
- [ ] I understand that debugging is a normal part of programming

---

## 📝 Knowledge Check

Test your understanding by answering these questions:

1. What is the difference between a SyntaxError and a NameError?
   - Your answer: ________________________________________

2. What does a TypeError usually indicate?
   - Your answer: ________________________________________

3. How do you fix an IndexError?
   - Your answer: ________________________________________

4. What is a logic error and why is it hard to find?
   - Your answer: ________________________________________

5. What is the first thing you should do when you see an error message?
   - Your answer: ________________________________________

6. How do you add a breakpoint in pdb?
   - Your answer: ________________________________________

7. What pdb command would you use to see the value of a variable?
   - Your answer: ________________________________________

8. How do you set a breakpoint in VS Code?
   - Your answer: ________________________________________

---

## 🎯 Final Validation

Before moving to Phase 1, complete the following:

- [ ] All exercises in `exercises/` folder are complete and working
- [ ] I understand all the concepts in `resources/common_errors.md`
- [ ] I've read and understand `resources/debugging_cheat_sheet.md`
- [ ] I can use the VS Code debugger effectively
- [ ] I feel confident about debugging Python code

---

## 📚 Additional Practice (Optional)

If you want more practice, try these:

1. Write a function that intentionally has a bug, then debug it
2. Find a Python script online and try to break it, then fix it
3. Practice using the VS Code debugger with your own code
4. Read about other Python exceptions (ValueError, AttributeError, etc.)

---

## 🎉 Ready for Phase 1?

If you've completed all the checklists above, you're ready to move on to **Phase 1: Pure Python Fundamentals**!

**Next Step:** Navigate to `/phase_1_cli_todo/README.md`

---

*Checklist last updated: [Date]*
*Phase 0 Status: [ ] In Progress  [ ] Complete
