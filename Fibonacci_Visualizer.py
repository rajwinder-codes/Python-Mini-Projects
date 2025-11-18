from flask import Flask , redirect , render_template , request , flash , url_for , session
import ast
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
app = Flask(__name__)
app.secret_key = "App_secret_key"
Data = {}
Fibonacci_List = []
@app.route("/" , methods=["POST" , "GET"])
def Sign_Up_Page():
    if request.method == "POST":
        try:
            with open("Data.txt" , "r") as f:
                Updated_Data = f.read()
                Data.update(ast.literal_eval(Updated_Data))
        except:
            flash("Sign Up With ur Username And Pass Pls!")
            return redirect(url_for("Sign_Up_Page"))
        else:
            Username = request.form.get("Username")
            Password = request.form.get("Password")
            if Username in Data :
                flash("User Already Registered, Pls Login!")
                return redirect(url_for("Login"))
            else:
                Data[Username] = {"Password" : Password , "Users_App_Data" : []}
                with open('Data.txt', 'w') as f:
                    f.write(str(Data))
                flash("Sign Up Successful, Pls Login!")
                return redirect(url_for("Login"))       
    return render_template("Sign_Up.html") 
@app.route("/Login" , methods=["POST" , "GET"])
def Login():
    try:
        with open("Data.txt" , "r") as f:
            Updated_Data = f.read()
            Data.update(ast.literal_eval(Updated_Data))
    except:
        flash("No User Found, Pls Sign Up First!")
        return redirect(url_for("Sign_Up_Page"))
    else:
        if request.method == "POST":
            Username = request.form.get("Username")
            Password = request.form.get("Password")
            if Username not in Data:
                flash("Username Not Found, Pls Enter Correct Username")
                return redirect(url_for("Login"))
            else:
                if Password != Data[Username]["Password"]:
                    flash("Incorrect Pass, Pls Enter Correct Pass!")
                    return redirect(url_for("Login"))
                else:
                    flash(f"Login Successful, Welcome {Username}")
                    return redirect(url_for("Home"))
        return render_template("Login.html")         
@app.route("/Home" , methods=["POST" , "GET"])
def Home():
    if request.method == "POST":
        try:
            User_Input = int(request.form.get("User_Input"))
        except:
            flash("Invalid Input, Pls Try Again Later!")
            return redirect(url_for("Home"))
        else:
            session['User_Input'] = User_Input
            return redirect(url_for("Output"))
    return render_template("Home.html")
@app.route("/Output" , methods = ["POST" , "GET"])
def Output():
    if request.method == "GET":
        User_Input = session.get('User_Input', 0)
        Formula(User_Input)
        Output = Fibonacci_List_Print(Fibonacci_List)
        plt.figure()
        plt.title("Fibonacci Sequence Visualization")
        plt.plot(Fibonacci_List , marker='o')
        plt.savefig("static/fibonacci_plot.png")
        plt.close()
        return render_template("Output.html" , Output = Output)

def Formula(User_Input):
    global Fibonacci_List
    a, b = 0, 1
    Fibonacci_List = [a, b]
    if User_Input > 2:
        User_Input +=1    
    for _ in range(2, User_Input):
        c = a + b
        Fibonacci_List.append(c)
        a, b = b, c
    if User_Input == 1:
        Fibonacci_List.pop(1)
    elif len(Fibonacci_List) > 2:
        Fibonacci_List.pop(2)    
        

def Fibonacci_List_Print(Fibonacci_List):
    Output = "Fibonacci No List : "
    for value in Fibonacci_List:
        Output += str(value) + " "
    return Output


        
app.run()