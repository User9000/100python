

#Creat a script that lets the user sumbit a password until they have satisfied ocnfitions:

file = open("usernamex.txt","r")
##read each line and put it inside a list
users = file.readlines()
###remove enters (lines)
users = [i.strip("\n") for i in users]
###convert every word to uppercase
users = [i.upper()  for i in users]

while True:
    username=input("Enter Username: ")
    #set the username to upper case and check to see if it exist in db
    if username.upper() in users:
        print("try another user")
        continue
    else:
        print("Good Username")
        break
      
while True:
    var = 0 
    password=input("Enter password: ")
    if not any(i.isdigit() for i in password):
        print("Need at least one digit")
        var = var + 1
         
    if not any(i.isupper() for i in password):
        print("Needs at least one uppercase letter") 
        var = var + 1
    if len(password) < 5:
        print("Password Should be greater than 5 characters")
        var = var + 1

    if var != 0:
        print("Try again")
    else:
        print("Password Accepted")
        break