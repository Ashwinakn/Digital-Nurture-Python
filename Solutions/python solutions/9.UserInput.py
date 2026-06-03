def read(name):
    if  name.strip() == "":
        print("Invalid Input")
    else:
        print("Welcome",name)
name=input("Enter user name:")
read(name)
