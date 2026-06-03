class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests software")

employees = [Developer(), Tester()]

for emp in employees:
    emp.work()
