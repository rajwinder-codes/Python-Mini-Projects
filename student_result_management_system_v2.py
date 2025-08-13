from flask import Flask , redirect, Response, url_for, request, session
import pandas as pd
import ast
data = {}
app = "student_result_management_system_v2"
app = Flask(__name__)
app.secret_key = "sidhu"
# Function To Get Grade
def Grade(marks):
    if marks >= 95:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "E"
# Function To Get Status
def Status(marks):
    if marks >= 40:
        return "Passs"
    else:
        return "Fail" 
# Percentage Method
def Percentage(a , b , c , d, e):
    total = a+b+c+d+e
    return total/5
# Total Marks Method
def Total_marks(a , b ,c , d ,e):
    return a+b+c+d+e
# Sign Up Page (Main Page)
@app.route("/" , methods =["GET", "POST"])
def Sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session["user"] = username
        if username in data :
            return Response("User Already Registered , Pls Login!")
        else:    
            data[username] = {"password" : password , "student_details" : []}
            with open("student_data.txt" , "w") as f:
                f.write(str(data))
            return redirect(url_for("Login"))
    return'''
        <h1>Student Result Management</h1>
        <form method = "POST">
        Username : <input type="text" name="username"><br><br>
        Password : <input type="text" name="password"><br><br>
        <input type="submit" value="Sign Up"> 
        </form>
    ''' 
# Login Page 
@app.route("/login" , methods=["GET" , "POST"])
def Login():
    with open("student_data.txt" , "r") as f:
        red = f.read()
        data.update(ast.literal_eval(red)) 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in data and password == data[username]["password"]:
            return redirect(url_for("Menu_page"))
        else:
            return Response("Pls Sign Up , User Not Found!")
    return'''<h1>Student Result Management</h1>
        <form method = "POST">
        Username : <input type="text" name="username"><br><br>
        Password : <input type="text" name="password"><br><br>
        <input type="submit" value="Login"> 
        </form>
        '''
# Menu Page 
@app.route("/menu_page" , methods =["GET" , "Post"] )
def Menu_page():
    if request.method == "POST":
        choice = int(request.form.get("choice"))
        if choice == 1:
            return redirect(url_for("Add_student"))
        if choice == 2:
            return redirect(url_for("Report_card"))
        if choice == 3:
            return redirect(url_for("Class_analytics"))
        if choice == 4:
            session.pop("user" , None)
            return Response("GoodBye Sir!")
        else:
            return Response("Invalid Choice , Pls Try Again!")
    return'''
    <h1>Student Result Management</h1><br>
    <h2>Menu<h2><br>
    <form method="POST" >
    <pre>
    1. Add New Student
    2. Generate Report Card
    3. Class Analytics
    4. Logout
    </pre>
    Enter Your Choice
    <input type="text" name="choice"> 
    </form>
    '''
# Add New Student
@app.route("/add_student" , methods=["GET", "POST"])
def Add_student():
    username = session.get("user")

    if request.method == "POST":
        name = request.form.get("name")  
        rollno = request.form.get("rollno") 
        pymarks = int(request.form.get("pymarks"))   
        dsmarks = int(request.form.get("dsmarks"))   
        aimarks = int(request.form.get("aimarks"))   
        engmarks = int(request.form.get("engmarks"))   
        mathmarks = int(request.form.get("mathmarks"))
        pygrade = Grade(pymarks)
        enggrade = Grade(engmarks)
        aigrade = Grade(aimarks)
        mathgrade = Grade(mathmarks)
        dsgrade = Grade(dsmarks)
        pystatus = Status(pymarks)
        aistatus = Status(aimarks)
        engstatus = Status(engmarks)
        mathstatus = Status(mathmarks)
        dsstatus = Status(dsmarks)
        totalmarks = Total_marks(pymarks , engmarks, mathmarks, dsmarks, aimarks)
        percentage = Percentage(pymarks, engmarks, mathmarks, dsmarks , aimarks)
        if any(student["rollno"] == rollno for student in data[username]["student_details"]):
            return '''
                Roll No Already Added , Pls Try Again
                <a href="/menu_Page">Return To Menu </a> 
                '''
        else:
            details ={"Subjects" : ["Python" , "English" , "Math" , "DS" , "Ai"],
                      "Marks" : [pymarks , engmarks , mathmarks , dsmarks , aimarks],
                    "Grade" : [pygrade , enggrade , mathgrade , dsgrade , aigrade],
                    "Status" :[pystatus , engstatus , mathstatus , dsstatus , aistatus]}
            data[username]["student_details"].append({"name" : name , "rollno" : rollno, "student_data" : details , "total_marks" : totalmarks , "percentage" : percentage}) 
            with open("student_data.txt" , "w") as f:
                f.write(str(data))
            return redirect(url_for("Menu_page"))    
    return'''
    <h2>Add New Student</h2><br>
    <form method="POST">
    Student Name : <input type="text" name="name"><br>
    Roll No      : <input type="text" name="rollno"><br>
    Python Marks : <input type="text" name="pymarks"><br>
    DS Marks     : <input type="text" name="dsmarks"><br>
    AI Marks     : <input type="text" name="aimarks"><br>
    Eng Marks    : <input type="text" name="engmarks"><br>
    Math Marks   : <input type="text" name="mathmarks"><br>
    <input type="submit" value="Submit">
    </form>
''' 
@app.route("/report_card" , methods=["POST" , "GET"])
def Report_card():
    username = session.get("user")

    if not data[username]["student_details"]:
        return'''
        No Data Found , Pls Add Student Details First
        <a href="/menu_page">Menu </a>
        '''
    else:
        output = ""
        for details in data[username]["student_details"]:
            output += f"<h3>Name     : {details['name']}<br>"   
            output += f"Roll No      : {details['rollno']}"   
            output += pd.DataFrame(details['student_data']).to_html(index = False)
            output += f"Percentage   : {details['percentage']}" 
        return output
@app.route("/class_analytics" , methods = ["POST", "GET"])
def Class_analytics():
    username = session.get("user")
    if not data[username]["student_details"]:
        return '''
        No Data Found, Please Add Student Details First
        <a href="/menu_page">Menu</a>
       '''
    df = pd.DataFrame(data[username]["student_details"])
    topper_index = df['total_marks'].idxmax()
    topper_name = df.loc[topper_index, 'name']
    passed_count = (df['percentage'] >= 40).sum()
    failed_count = (df['percentage'] < 40).sum()
    output = ""
    output += f"<h3>Total Students: {len(df)}</h3>"
    output += f"<h3>Topper of Class: {topper_name}</h3>"
    output += f"<h3>No of Students Passed: {passed_count}</h3>"
    output += f"<h3>No of Students Failed: {failed_count}</h3>"

    return output

app.run()       

