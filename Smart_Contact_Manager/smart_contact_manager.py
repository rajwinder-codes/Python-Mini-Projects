print("\tWelcome to Smart Contact Manager")
contact = {}
print("Choose an option: ")
print("1. Add Contact")
print("2. Search Contact")
print("3. Delete Contact")
print("4. Show All Contacts")
print("5. Exit")

option = int(input("Enter choice: "))
if option == 1:
    name = input("Enter Name: ")
    no = int(input("Enter Number: "))
    contact.update({name : no})
    print("Contact Added Succesfully")
elif option == 2:
    name = input("Enter the Name: ")
    print(contact.get(name))   
elif option == 3:
    name = input("Enter the Name: ")
    if name in contact:
        del contact[name]
        print("Contact Deleted Succesfully")
    else :
        print("No Contact Found Recheck The Name")   
elif option == 4:
    print(contact)
elif option == 5:
    print("Exiting....")
    exit()        
elif option >=6:
    print("Please Enter Correct Option")
    exit()        
elif option <=0:
    print("Please Enter Correct Option")

    exit()        
