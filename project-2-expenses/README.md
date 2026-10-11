# Project 2: Expense Tracker

## 🎯 Goal
Learn data structures by tracking expenses.

---

## 📌 Start Here (Simple Version)

```python
# expenses.py - Track your spending
expenses = []

def add():
    amount = float(input("Amount: "))
    description = input("Description: ")
    expenses.append({"amount": amount, "description": description})

def view():
    for exp in expenses:
        print(f"${exp['amount']:.2f} - {exp['description']}")

def total():
    print(f"Total: ${sum(e['amount'] for e in expenses):.2f}")

while True:
    print("\n1. Add  2. View  3. Total  4. Quit")
    choice = input("> ")
    if choice == "1": add()
    elif choice == "2": view()
    elif choice == "3": total()
    elif choice == "4": break
```

Save as `project-2-expenses/expenses.py`

---

## 🚀 Next Steps

1. **Add categories**
   - Track what type of expense (Food, Transport, etc.)

2. **Add dates**
   - When was the expense?

3. **Save to file**
   - Save expenses to CSV or JSON

4. **Monthly reports**
   - Show spending by month

5. **Income tracking**
   - Track both expenses AND income

---

## 💡 Tips

- Start simple, then improve
- Use dictionaries to store expense details
- Try CSV format for file saving
- Test each feature as you add it
