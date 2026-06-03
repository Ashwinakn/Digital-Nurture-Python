class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)

e1 = Employee("John")
e2 = Employee("David")

e1.display()
e2.display()
