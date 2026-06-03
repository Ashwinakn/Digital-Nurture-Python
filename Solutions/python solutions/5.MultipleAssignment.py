def unpack(coords):
    x,y=coords
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        print("Invalid Coordinates")
    else:
        print("X coordinates:{:.2f}".format(x))
        print("Y coordinates:{:.2f}".format(y))
        
coords=(10,20)
unpack(coords)
