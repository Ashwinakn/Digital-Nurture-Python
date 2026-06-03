class Employee:
    def __init__(self):
        self.salary = 0

    def set_salary(self, amount):
        if amount > 0:
            self.salary = amount
        return self

    def raise_salary(self, amount):
        if amount > 0:
            self.salary += amount
        return self

    def display(self):
        print("Final Salary:", self.salary)

emp = Employee()

emp.set_salary(5000).raise_salary(2000).display()
