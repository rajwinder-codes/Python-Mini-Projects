import pandas as pd
import ast
data = {}
def Register_user():
    username = input("Enter Your Username: ")
    if username in data: 
        print("User Already Registered , Pls Login!")
    else:     
        password = input("Enter Your Password: ")
        print("Registeration Successsfull!")
        data[username] = {"password" : password , "student_details" : []}
        with open("Student.txt" , "w") as f:
            f.write(str(data))
def get_grade(marks):
    if marks >= 95:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 40:
        return "C"
    elif marks >= 35:
        return "E"
    else:
        return "F"
def Status(marks):
    if marks >= 35:
        return "Passed"
    else :
        return "Failed"
def Final_result(a , b , c , d , e):
    if a >=35 and b >=35 and c >=35 and d >=35 and e >=35 :
        return "Passed" 
    else:
        return "Failed"
def Login_user():
    try:
        with open("Student.txt" , "r") as f:
            red = f.read()
            data.update(ast.literal_eval(red))
    except:
        print("No Data Found , Pls Register!")   
    else:     
        username = input("Enter Your Username: ")
        if username in data:
            password = input("Enter Ur Pass: ")
            if password == data[username]["password"]:
                print("Login Successfull!")
                while True:
                    print("\n1. Add New Student")
                    print("2. Generate Report Cards")
                    print("3. Exit")
                    try:
                        choice = int(input("Enter Your Choice: "))
                    except :
                        print("Error , Choose A Valid Option")
                    else:
                        if choice == 1:
                            name = input("Enter Student Name: ").title()
                            rollno = input("Enter Student Rollno: ")
                            try:
                                pymarks = int(input("Enter Marks in python: "))
                                mathmarks = int(input("Enter Marks in Math: "))
                                engmarks = int(input("Enter Marks in English: "))
                                aimarks = int(input("Enter Marks in AI: "))
                                dsmarks = int(input("Enter Marks in DS: "))
                            except:
                                print("Error , Pls Enter Valid Marks")  
                            else:
                                pygrade = get_grade(pymarks)
                                mathgrade = get_grade(mathmarks)
                                enggrade = get_grade(engmarks)
                                aigrade = get_grade(aimarks)
                                dsgrade = get_grade(dsmarks)
                                pystatus = Status(pymarks)
                                mathstatus = Status(mathmarks)
                                engstatus = Status(engmarks)
                                aistatus = Status(aimarks)
                                dsstatus = Status(dsmarks)
                                totalmarks = pymarks + mathmarks + engmarks + aimarks + dsmarks
                                percentage = totalmarks/5 
                                finalresult = Final_result(pymarks , mathmarks , engmarks , aimarks , dsmarks)
                                marks = {"Subjects" : ["Python" , "Math" , "English" , "AI" , "DS"] , 
                                        "Marks" : [pymarks , mathmarks , engmarks , aimarks , dsmarks],
                                        "Grades" :[pygrade , mathgrade , enggrade , aigrade , dsgrade],
                                        "Status" :[pystatus , mathstatus , engstatus , aistatus , dsstatus]
                                        }
                                markdetails = pd.DataFrame(marks)
                                marks_dic = markdetails.to_dict()
                                data[username]["student_details"].append({"rollno" : rollno ,"name" : name , "marks" : marks_dic , "percentage" : percentage , "finalresult" : finalresult})
                                with open("Student.txt" , "w") as f:
                                    f.write(str(data))
                        elif choice == 2: 
                            if not data[username]['student_details']:
                                print("No Data Found")
                            else:
                                print("Report Card") 
                                for details in data[username]["student_details"]:
                                    print(f"Name           : {details['name']}")   
                                    print(f"Roll No        : {details['rollno']}")   
                                    marksdf = pd.DataFrame(details['marks'])
                                    marksdf = marksdf[['Subjects', 'Marks', 'Grades', 'Status']]
                                    print(marksdf)
                                    print(f"Final Result : {details['finalresult']}")          
                                    print(f"Percentage   : {details['percentage']}") 
                        elif choice == 3:
                            print("GoodBye....")
                            exit()     
                        else:
                            print("Error , Pls Enter A Valid Option")                    
                else:
                    print("Pass Incorrect , Pls Try Again!")
            else:
                print("User Not Found , Pls Try Again!")            

while True:
    print("------------------------------------------------------------------")
    print("             Student Result Management System")
    print("------------------------------------------------------------------")
    print("\n1. Register Admin")
    print("2. Login")
    print("3. Exit")
    try:
        choice = int(input("Enter Your Choice: "))
    except :
        print("Error , Choose A Valid Option")
    else:
        if choice == 1:
            Register_user()
        elif choice == 2:
            Login_user()
        elif choice ==3:
            break
        else:
            print("Error , Pls Enter A Valid Option")    
               
