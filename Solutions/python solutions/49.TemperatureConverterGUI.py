class Converter:
    @staticmethod
    def c_to_f(c):
        return c * 9/5 + 32
    
    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5/9

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice (1/2): ") or "1"
    temp = float(input("Enter temperature: ") or "0")
    if choice == '1':
        print(f"Result: {Converter.c_to_f(temp):.2f} F")
    elif choice == '2':
        print(f"Result: {Converter.f_to_c(temp):.2f} C")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
