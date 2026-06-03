import math as m
def areaofcircle(radius):
    area= m.pi * (radius*radius)
    print("Area of the Circle: {:.2f} m² ".format(area))
r=float(input("Enter the radius:"))
areaofcircle(r)
