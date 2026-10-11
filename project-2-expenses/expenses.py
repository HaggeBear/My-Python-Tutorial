# Expense Tracker - Starter Code
# Save this as: project-2-expenses/expenses.py

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
