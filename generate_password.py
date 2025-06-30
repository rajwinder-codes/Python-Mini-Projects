import string
print("SECURE PASSWORD GENERATOR")
a = input("Desired Password (Minimum 8 Letters)")
if len(a)>=8:
    b = input("Enter A Special Symbol ")
if len(a)<8:
    print("Pass too Short Try Again")
    exit()   
if b in string.punctuation:
    c = input("Enter Uppercase Letter ")
if b not in string.punctuation :
    print("NO Special Symbol Try Again")
    exit()
if c.isupper():
    d = input("Enter a Digit ")
else :
    print("Try Again NO Uppercase")
    exit()
if d.isdigit():
    print(f"Pass is {a+b+c+d}")
else :
    print("No Digits Try Again")
    exit()
        
 