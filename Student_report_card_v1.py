print("\tStudent Report Card")
d = {}
div = set()
no = int(input("How many students? "))
# MAX ONLY 2 STUDENTS BCZ v1 IS WITHOUT LOOP

if no == 1:
    print("Student 1:")
    mar1 = []
    no1 = input("Name: ")
    rol1 = input("Roll No: ")
    mar1.append(int(input("Marks in subject 1: ")))
    mar1.append(int(input("Marks in subject 2: ")))
    mar1.append(int(input("Marks in subject 3: ")))
    total1 = sum(mar1)
    d.update({no1 : total1})
    div.add(rol1)
    print(f"Total: ",total1)
    average = total1/3 
    print(f"Average: ",average) 
    if average >=90:
        print("Grade: A+")
        print("Excellent")
    elif average >=80:
        print("Grade: A")
        print("Very Good")
    elif average >=70:
        print("Grade: B") 
    elif average >=60:
        print("Grade: C")
        print("Satisfactory")       
    elif average >=50:
        print("Grade: D")
        print("Need Improvement")
    elif average >= 33:
        print("Grade: E")
        print("Pass but Weak")
    elif average < 33:
        print("Grade: F")
        print("Fail")
if no == 2:   
    print("Student 1:")
    mar1 = []
    no1 = input("Name: ")
    rol1 = input("Roll No: ")
    mar1.append(int(input("Marks in subject 1: ")))
    mar1.append(int(input("Marks in subject 2: ")))
    mar1.append(int(input("Marks in subject 3: ")))
    total1 = sum(mar1)
    d.update({no1 : total1})
    div.add(rol1)
    print(f"Total: ",total1)
    average = total1/3 
    print(f"Average: ",average) 
    if average >=90:
        print("Grade: A+")
        print("Excellent")
    elif average >=80:
        print("Grade: A")
        print("Very Good")
    elif average >=70:
        print("Grade: B") 
    elif average >=60:
        print("Grade: C")
        print("Satisfactory")       
    elif average >=50:
        print("Grade: D")
        print("Need Improvement")
    elif average >= 33:
        print("Grade: E")
        print("Pass but Weak")
    elif average < 33:
        print("Grade: F")
        print("Fail")    
        
    print("Student 2:")
    mar2 = []
    no2 = input("Name: ")
    rol2 = input("Roll No: ")
    mar2.append(int(input("Marks in subject 1: ")))
    mar2.append(int(input("Marks in subject 2: ")))
    mar2.append(int(input("Marks in subject 3: ")))
    total2 = sum(mar2)
    d.update({no2 : total2})
    div.add(rol2)
    print(f"Total: ",total2)
    average2 = total2/3 
    print(f"Average: ",average2) 
    if average2 >=90:
        print("Grade: A+")
        print("Excellent")
    elif average2 >=80:
        print("Grade: A")
        print("Very Good")
    elif average2 >=70:
        print("Grade: B") 
    elif average2 >=60:
        print("Grade: C")
        print("Satisfactory")       
    elif average2 >=50:
        print("Grade: D")
       
        print("Need Improvement")
    elif average2 >= 33:
        print("Grade: E")
        print("Pass but Weak")
    elif average2 < 33:
        print("Grade: F")
        print("Fail")