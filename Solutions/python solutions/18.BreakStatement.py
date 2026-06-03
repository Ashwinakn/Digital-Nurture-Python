def findeve(start,end):
    if start>=end:
        print("Invalid Input")
    else:
        for i in range(start,end+1):
            if i%2==0:
                print(i,"is the first even number for the given range")
                break
start=int(input("Enter the start of range:"))
end=int(input("Enter the end of the range:"))
findeve(start,end)
