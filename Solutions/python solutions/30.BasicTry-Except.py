def divide(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

divide(x, y)
