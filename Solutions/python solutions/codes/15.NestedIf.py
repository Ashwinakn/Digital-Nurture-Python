def func(username,password):
    if username.strip() == "" or password.strip() == "":
        print("Invalid.Empty Inputs")
    else:
        if username == "admin":
            if password == "pass123":
                print("Valid.Login Successful!")
            else:
                print("Invalid")
        else:
            print("Invalid")
user=input("Enter username:")
pwd=input("Enter password:")
func(user,pwd)
