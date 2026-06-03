def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operation.")

def main():
    try:
        a = float(input("Enter first number: ") or "10")
        b = float(input("Enter second number: ") or "5")
        op = input("Enter operation (+, -, *, /): ") or "+"
        res = calculate(a, b, op)
        print(f"Result: {res}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print("Invalid input.")

if __name__ == "__main__":
    main()
