def area(length, width):
    if length <= 0 or width <= 0:
        return "Invalid Input"
    
    a = length * width
    return a

result = area(5, 3)
print("Area:", result)
