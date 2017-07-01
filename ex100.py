

#create a web app in where you add lines same as ex98 but with a webapp

from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')

def home():
    return render_template("password.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    username = request.form['username']
    password = request.form['password']
    ##################################################
    file = open("usernamex.txt","r")
    ##read each line and put it inside a list
    users = file.readlines()
    ###remove enters (lines)
    users = [i.strip("\n") for i in users]
    ###convert every word to uppercase
    users = [i.upper()  for i in users]

    while True:
        #username=input("Enter Username: ")
        #set the username to upper case and check to see if it exist in db
        if username.upper() not in users:
            print("try another user")
            warning_username = "Try another user"
            break
        else:
            print("Good Username")
            warning_username = "Good Username"
            break
        
    while True:
        var = 0 
        #password=input("Enter password: ")
        if not any(i.isdigit() for i in password):
            print("Need at least one digit")
            warning_username = "Neet at least one digit"
            var = var + 1
            break
            
        if not any(i.isupper() for i in password):
            print("Needs at least one uppercase letter") 
            var = var + 1
            warning_password = "Needs at least one uppercase letter"
            break
        if len(password) < 5:
            print("Password Should be greater than 5 characters")
            var = var + 1
            warning_password = "Password should be greater than 5 characters"
            break

        if var != 0:
            print("Try again")
            warning_password = "Try again"
            break
        else:
            #print("Password Accepted")
            warning_password = "Password Accepted"
            break
    

    ##################################################
    username =None
    password = None
    return render_template("password.html",warning_password = warning_password, warning_username= warning_username )

if __name__=="__main__":
    app.run(debug=True)

