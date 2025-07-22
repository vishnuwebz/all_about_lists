# 2 mini project 2: expense tracker

expenses = [1000, 2500, 800]

def track_expenses():
    expenses.append(float(input("Enter new expense: ")))
    total = sum(expenses)
    print(f"Expenses: {expenses}, Total: {total: .2f}")
track_expenses()

"""
Enter new expense: 200
Expenses: [1000, 2500, 800, 200.0], Total:  4500.00
"""