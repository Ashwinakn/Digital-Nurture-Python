def floorDiv(total_bill,people):
    if isinstance(total_bill,(int,float)) and isinstance(people,int):
        print("Bill per person:",total_bill//people)
total_bill=1250
people = 4
floorDiv(total_bill,people)
