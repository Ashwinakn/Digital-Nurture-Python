def marks(marks):
    if marks<25 and marks<=50:
        print("C Grade")
    elif marks>50 and marks<=85:
        print("B Grade")
    elif marks>85 and marks<=100:
        print("A Grade")
    else:
        print("Fail")
m= 88
marks(m)
