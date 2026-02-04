import ast
userdata = {}
class Userdetails():
    def Registeruser(self):
        name = input("Enter Ur Full Name: ").title()
        username = input("Choose Username: ")
        if username in userdata:
            print("Username Already Taken , Pls Try Again!")
        else :
            password = input("Choose Password: ")
            print("User Registered Successfully!")
            userdata[username] = {"name" : name , "password" : password , "expenses" : [] , "totalspend" : 0}   
            with open(f"{username}.txt" , "w") as f:
                f.write(str(userdata)) 
    def Loginuser(self):
        username = input("Enter Your Username: ")
        try:
            with open(f"{username}.txt") as f:
                data =f.read()
                userdata.update(ast.literal_eval(data))
        except:         
            print("Useranme Not Found , Pls Try Again!")
        else: 
            password = input("Enter Your Pass: ")
        
            if password != userdata[username]["password"]:
                print("Password Incorrect , Pls Try Again!")
            else :
                print(f"Login Successful. Welcome , {userdata[username]['name']}")  
                while True:
                    print("\n----------------------------------------------------------------------")  
                    print(f"        Expense Tracker Menu ({userdata[username]['name']})")
                    print("----------------------------------------------------------------------") 
                    print("1. Add Expense")
                    print("2. View All Expenses")
                    print("3. Delete An Expense")
                    print("4. Total spend")
                    print("5. Save Expenses To File")
                    print("6. Load Expenses From File")
                    print("7. Logout")
                    totalspend = userdata[username].get("totalspend")
                    try:
                        choice = int(input("\nEnter Your Choice: "))
                    except:
                        print("Error , Pls Enter A Valid Choice!") 
                    else:                              
                        if choice == 1:
                            try:
                                amount = int(input("\nEnter Amount: "))
                            except:
                                print("Error , Pls Enter A Vaild Amount!")
                            else:
                                category = input("Enter Title: ")
                                date = input("Enter Date(YYYY-MM-DD): ")
                                userdata[username]['totalspend'] += amount
                                totalspend = userdata[username]["totalspend"] 
                                userdata[username]['expenses'].append({"amount" : amount , "category" : category , "date" : date})
                                print(f"Expense Added Successfully For {date}")
                        elif choice == 2:
                            print(f"Total Expense Amount: {userdata[username]['totalspend']}")
                            if not userdata[username]['expenses']:
                                print("NO Expenses Found")
                            else:
                                print("All Expenses: ")
                                for expense in userdata[username]["expenses"]:
                                    print(f"Category : {expense['category']} | Amount : {expense['amount']} | Date : {expense['date']}")     
                        elif choice == 3:
                            category = input("Enter Title To Dlt: ")
                            found = False
                            for expense in userdata[username]['expenses']:
                                if expense['category'] == category:
                                    userdata[username]["totalspend"] -= expense["amount"]
                                    userdata[username]["expenses"].remove(expense)
                                    totalspend = userdata[username]["totalspend"]
                                    found = True 
                                    print("Expense Deleted Succuessfully!")
                            if not found:
                                print("No Expense Found For Title!") 
                        elif choice == 4:
                            print(f"Total Spend: {userdata[username]['totalspend']}")
                        elif choice == 5:
                            print("Data Saved Successfully!")    
                            with open(f"{username}.txt" , "w") as f:
                                f.write(str(userdata))
                        elif choice == 6:
                            with open(f"{username}.txt") as f:
                                data =f.read()
                                userdata.update(ast.literal_eval(data))  
                                print("Data Loaded Successfully!")       
                        elif choice == 7:
                            print("Loging Out.... Goodbye!")
                            break
                        else:
                            print("Error , Pls Choose The Correct Option!")    

while True:
    print("------------------------------------------------------------")
    print("           Welcome To Daily Expense Tracker")
    print("------------------------------------------------------------")
    print("\n1. Register New User")
    print("2. Login To Ur Account")
    print("3. Exit")
    try:
        choice = int(input("Enter Choice: "))
    except:
        print("Error! Pls Enter Valid Option") 
    else:       
        if choice == 1:
            Userdetails().Registeruser()     
        elif choice == 2:
            Userdetails().Loginuser()
        elif choice == 3:
           print("Exiting.... Goodbye!")
           break    
        else:
           print("Error , Pls Choose The Correct Option!")    

