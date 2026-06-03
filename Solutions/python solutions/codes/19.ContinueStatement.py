def addodd(n):
    if n<=0:
        print("")
    else:
        s=0
        for i in range(10):
                if i%2==0:
                    continue
                else:
                    s+=i
        print("The sum of all the Odd number of the given range is: ",s)
n=10
addodd(n)
