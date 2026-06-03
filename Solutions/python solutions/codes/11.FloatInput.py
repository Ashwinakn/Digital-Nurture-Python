def convert(kg):
    if not isinstance(kg,float):
        print("Invalid Input")
    else:
        lbs=kg*2.20462
        print("The weight in pounds: {:.3f} pounds".format(lbs))
kgs=float(input("Enter weight in kgs:"))
convert(kgs)
