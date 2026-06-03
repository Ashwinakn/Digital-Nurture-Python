def age(a):
    if isinstance(a,int):
          print("Next year you'll be",a+1)
    else:
        print("Invalid Input")
ag=input("Enter your age:")
age(int(ag))
