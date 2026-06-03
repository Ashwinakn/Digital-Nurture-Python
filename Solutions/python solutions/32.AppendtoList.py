def add_expense(amount):
    expenses = [100, 250, 75]

    if amount <= 0:
        print("Invalid Expense Amount")
    else:
        expenses.append(amount)
        print("Updated Expenses List:", expenses)

amt = int(input("Enter expense amount: "))
add_expense(amt)
