data = {}
while True:
    print("-------------------------------------")
    print("  STUDENT MANAGEMENT SYSTEM - v1.0")
    print("-------------------------------------")
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Save to File")
    print("7. Load from File")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        rollno = int(input("Enter roll number: "))
        name = input("Enter name: ").capitalize()
        marks = int(input("Enter marks: "))  
        data[rollno] = {"Name" : name , "Marks" : marks}
        print("Student Added Successfully!")
    elif choice == 2:
        print("All Students:")
        for rollno, details in data.items():
            print("--------------------------------------")  
            print(f"Name : {details['Name']} | Roll NO : {rollno} | Marks : {details['Marks']}")  
            print("--------------------------------------")    
        if not data:
            print("No Student Data Found")
    elif choice == 3:
        rollno = int(input("Enter roll number to search: "))
        for rollno , details in data.items():
            if rollno in data:
                print("Student Found:")
                print(f"Roll No : {rollno} | Name : {details['Name']} | Marks : {'Marks'}")
            else :
                print("No Data Found For The Roll No")
    elif choice == 4:
        rollno = int(input("Enter roll no to update: "))
        if rollno in data:
            data[rollno]["Name"] = input("Enter New Name: ").capitalize()
            data[rollno]["Marks"] = int(input("Enter New Marks: "))
            print("Student Details Updated Successfully!")
        else :
            print("No Similar Roll No Found")    
    elif choice == 5:
        rollno = int(input("Enter roll no to delete: "))
        if rollno in data:
            del data[rollno]
            print("Data Deleted Successfully!")
        else:
            print("No Data Found For Roll NO ")
    elif choice == 6:
        with open("students.txt" , "w" ) as f:
            savedata = str(data)
            f.write(savedata)
        print("Saving data to file....")    
        print("Data saved to file 'students.txt' ")
    elif choice == 7:
        with open("students.txt") as f:
            saveddata = f.read()
            print(saveddata)
    elif choice == 8:
        print("Exiting... Goodbye")

        break
