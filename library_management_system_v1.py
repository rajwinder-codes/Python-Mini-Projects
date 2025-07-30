Books = {} 
Members = {}
Booksborrowed = {}
class book():
    def addbook(self):    
        Bookname = input("Enter Book Title: ").title()
        Authorname = input("Enter Author Name: ").title()
        Totalcopies = int(input("Enter Total Copies: "))
        if Bookname in Books:
            Books[Bookname]['Totalcopies'] += Totalcopies  
            Books[Bookname]['Availablecopies'] += Totalcopies  
            print("Book Updated Successfully!") 
        else: 
            Books[Bookname] = {"Authorname" : Authorname , "Totalcopies" : Totalcopies , "Availablecopies" : Totalcopies}
            print(f"{Bookname} Added Successfully!")
    def allbooks():
        print("All Books: ")
        for Bookname , details in Books.items():
            print(f"Bookname : {Bookname} | Authorname : {details['Authorname']} | {details['Totalcopies']}/{details['Availablecopies']}")        
class members():
    def addmember(self):      
        name = input("Enter Your Full Name: ").title() 
        username = input("Enter The Username U Want: ")
        password = input("Enter The Pass: ") 
        if username in Members:
            print("Username Already Taken , Pls Try Again!") 
        else :
            Members[username] = {"password" : password , "name" : name}
            print("Member Registered Successfully!")
    def allmembers():    
        print("All Members: ")
        for username , details in Members.items():
            print(f"Name : {details['name']} | Username : {username}")
        if not Members:
            print("No Users Found!") 
    def borrowbook(self):
        Bookname = input("Enter Book Name To Borrow: ").title()
        if Bookname not in Books:
            print("Book Not Available")
        else :
            if Books[Bookname]['Availablecopies'] != 0:
                username = input("Enter Your Username: ")
                if username in Members:
                    password = input("Enter Your Password")
                    if password == Members[username]['password']:
                        print("Book Borrow Successfull!")
                        name = Members[username]['name']  
                        Booksborrowed[username] = {"bookborrowed" : Bookname , "name" : name}
                        Books[Bookname]['Availablecopies'] -= 1
                    else:
                        print("Pass is Wrong , Pls Try Again!")  
                else:
                    print("Username Not Found Pls Register First")   
            else:
                print(f"{Bookname} Is Not Available Currently , Out Of Stock")  
    def returnbook(self):
        Bookname = input("Enter Book Nmae To Return: ").title()   
        if Bookname in Booksborrowed:
            username = input("Enter ur Username: ")
            if username not in Booksborrowed:
                print("The User Has Not Borrowed The Book!")
            else:     
                print(f"{Bookname} Returned Successfully!")
            del Booksborrowed[username]["Bookname"]
            Books[Bookname]["Availablecopies"] += 1
        else:
            print(f"{Bookname} Is Not Borrowed From Library , Pls Check Name And Try Again!")    
class file():
    def savedata():
        with open("library.txt" , "w") as f:
            f.write(str(Books))
            f.write(str(Booksborrowed))
            f.write(str(members))
        print("Saving Data To File....")
        print("Data Uploaded Successfully!") 
    def loaddata():
        with open("library.txt") as f:
            print(f.read())        
while True:
    print("Welcome To Library Management & Membership System")
    print("1. Add Book (Admin)")
    print("2. Register Member (User)")
    print("3. Borrow Book (User)")
    print("4. Return Book (User)")
    print("5. Show All Books")
    print("6. Show All Members")
    print("7. Save Data To File")
    print("8. Load Data From File")
    print("9. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        book().addbook()
    elif choice == 2:
        members().addmember()    
    elif choice == 3:
        members().borrowbook()  
    elif choice == 4:
        members().returnbook()
    elif choice == 5:
        book().allbooks()
    elif choice == 6:
        members().allmembers()    
    elif choice == 7:
        file().savedata()
    elif choice == 8:
        file().loaddata()
    elif choice == 9:
        break
    else :
        print("Error! Pls Choose The Correct Option")            