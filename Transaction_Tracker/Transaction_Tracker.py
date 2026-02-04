print("/tWelcome To Transaction Tracker v1")

d = 0
c = 0
# history = []
print("1. Add Income")
print("2. Add Expense")
print("3. Show Balance")
print("4. View All Transactions")
print("5. Exit")

# NO LOOPS yet will be in v2
a = int(input("Choose an option: "))
if a == 1: 
    income = int(input("Enter income amount: "))
    # history.append(f"Icome: {income}")
    c += income
    print(f"Icome of {income} added.")
elif a == 2:
    expense = int(input("Enter expense amount : "))
    d += expense
    # history.append(f"Expense: {expense}") 
    print(f"Expenses of {expense} added. ")
elif a == 3:
    b = c-d
    print(f"Current Balance: {b}")
elif a == 4:
    b = c-d    
    print("\tTransaction History:")
    print(f"- Income: {c}") 
    print(f"- Expenses: {d}")
    print(f"Net Balance: {b}")
elif a == 5:
    print("Exiting...")

    exit()    


