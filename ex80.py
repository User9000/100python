

#python PAM



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



