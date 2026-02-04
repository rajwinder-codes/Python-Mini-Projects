print("WELCOME TO SIDHU'S CALCULATOR")
# Input Both Numbers
a = int(input("Enter The First Number "))
b = int(input("Enter The Second Number "))
# OPERATIONS
print("\nCHOOSE THE OPERATION")
print("+  For Addition")
print("-  For Subtraction")
print("*  For Multiplication")
print("/  For Division")
print("** For Power ")
# Take Operation Symbol
c = input("Enter The Operation Symbol ") 
# Result
if c == "+": 
    d=b+a 
    print(f"Result = {a} + {b} = {d}")
elif c == "-":
    d = a - b
    print(f"Result = {a} - {b} = {d}")               
elif c == "*":
    d = a*b
    print(f"Result = {a} * {b} = {d}")
elif c == "/":
    if b !=0:
        d = a/b
        print(f"Result = {a} / {b} = {d}\n \tReminder = {a%b}")
    else: 
        print("ERROR , Division Of 0 is not Possible")
elif c == "**":
   d = a**b

   print(f"Result = {a} ** {b} = {d}")
