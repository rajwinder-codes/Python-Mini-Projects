print("==== Daily Expense Tracker ====")
data = {}
while True : 
    print("Choose An Option")
    print("1. Add Expense ")
    print("2. View All Expenses")
    print("3. View Total Spend")
    print("4. Delete An Expense")
    print("5. Exit")
    option = int(input("Enter Choice: "))
    if option == 1:
        name = input("Enter Expense Name: ").capitalize()
        spend = int(input("Enter Amount: "))
        data.update({name : spend})
        print("Expense Added!")
    elif option == 2:
        if not data:
            print("No Expense Recorded")
        else:
            for name, spend in data.items():
                print(f"{name} : {spend}")    
    elif option == 3:
        print(f"Total Spend: ",sum(data.values()))
    elif option == 4:
        name = input("Enter Expense Name: ").capitalize()
        if name in data:
            del data[name]
        else:
            print("No Expense Found")
    elif option == 5:
        print("Goodbye!")
        break
    else:

        print("Try Again Choose Correct Option")             
