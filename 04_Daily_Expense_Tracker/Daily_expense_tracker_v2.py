print("==== Daily Expense Tracker ====")
data = {}
while True:
    print("Choose An Option")
    print("1. Add Expense ")
    print("2. View All Expense")
    print("3. View Expense By Category")
    print("4. View Expense By Date")
    print("5. View Total Spend")
    print("6. Exit")
    option = int(input("Enter Choice "))
    if option == 1:
        name = input("Enter Expense Name: ").capitalize()
        spend = int(input("Enter Amount: "))
        category = input("Enter Category: ").capitalize()
        date = input("Enter Date (YYYY-MM-DD): ")
        data[name] = { "spend": spend, "category" : category, "date" : date}
        print("Expense Added!")
    elif option == 2:
        print("All Expenses:")
        for name, details in data.items():
            print(f"-{name} : {details["spend"]} | {details["category"]} | {details["date"]}")
        if not data:    
            print("No Expense Recorded")
    elif option == 3:
        category = input("Enter Category To Filter: ").capitalize()
        for name, details in data.items():
            if details["category"] == category:
                print(f"Expenses in Category {category}:")
                print(f"-{name}: {details["spend"]} on {details["date"]}")
            elif details["category"] != category:
                print("No Expense With Matching Category")
    elif option == 4:
        date = input("Enter Date (YYYY-MM-DD) To Filter: ")
        for name, details in data.items():
            if details["date"] == date:
                print(f"Expenses on Date {date}:")
                print(f"-{name}: {details["category"]} | {details["spend"]}")
            elif details["date"] != date :
                print(f"No Expense on Found on {date}")
    elif option == 5:
        total = sum(details["spend"] for details in data.values())
        print(total)
    elif option == 6:
        print("Exiting...")
        break
    else :
        print("Try Again And Choose The Correct Option!")
