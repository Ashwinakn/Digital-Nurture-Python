def func(a,b):
    if a>0:
        if b>a:
            print("Nested")
        else:
            print("Invalid")
    print("Function completed")
a=int(input())
b=int(input())
func(a,b)
