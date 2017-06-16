

#python PAM



while True:
    password=input("Enter password: ")
    if any(i.isdigit() for i in password) and any(i.upper() for i in password) and len(password) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")