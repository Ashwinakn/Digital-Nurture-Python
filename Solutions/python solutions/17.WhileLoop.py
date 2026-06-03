def loop(count):
    if count<=0:
        print("Invalid Input")
    else:
        while count>0:
            print(count,end=" ")
            count-=1
            
n=int(input())
loop(n)
