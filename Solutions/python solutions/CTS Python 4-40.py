#!/usr/bin/env python
# coding: utf-8

# 4. Float Precision

# In[6]:


def flprecision(salary,tax_rate):
    if not isinstance(salary,float) and not isinstance(tax_rate,float):
        print("Invalid Input")
    else:
        netsalary = salary * (1-tax_rate)
        print("Net Salary = {:.2f}".format(netsalary))
salary=75000.5
tax_rate=0.18
flprecision(salary,tax_rate)


# 5. Multiple Assignment

# In[5]:


def unpack(coords):
    x,y=coords
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        print("Invalid Coordinates")
    else:
        print("X coordinates:{:.2f}".format(x))
        print("Y coordinates:{:.2f}".format(y))
        
coords=(10,20)
unpack(coords)

    
    


# 6. Modulo Operator

# In[8]:


def modulo(num):
    if isinstance(num,int):
        if num%2==0:
            print(num," is Even")
        else:
            print(num,"is Odd")
number = 17
modulo(number)


# 7. Floor Divison

# In[9]:


def floorDiv(total_bill,people):
    if isinstance(total_bill,(int,float)) and isinstance(people,int):
        print("Bill per person:",total_bill//people)
total_bill=1250
people = 4
floorDiv(total_bill,people)


# 8. Min/Max Functions 

# In[13]:


def findminmax(list):
    salary=[]
    for i in list:
        if isinstance(i,(int,float)):
            salary.append(i)
    print(min(salary))
    print(max(salary))
s=[50000,75000,62000,95000]
findminmax(s)


# 9. User Input

# In[22]:


def read(name):
    if  name.strip() == "":
        print("Invalid Input")
    else:
        print("Welcome",name)
name=input("Enter user name:")
read(name)


# 10. Numeric Input

# In[27]:


def age(a):
    if isinstance(a,int):
          print("Next year you'll be",a+1)
    else:
        print("Invalid Input")
ag=input("Enter your age:")
age(int(ag))



# 11. Float Input

# In[32]:


def convert(kg):
    if not isinstance(kg,float):
        print("Invalid Input")
    else:
        lbs=kg*2.20462
        print("The weight in pounds: {:.3f} pounds".format(lbs))
kgs=float(input("Enter weight in kgs:"))
convert(kgs)


# In[ ]:


12. Simple If


# In[35]:


def marks(marks):
    if marks>=75:
        print("Pass")
        
m=int(input("Enter student marks:"))
marks(m)


# 13. If-Else

# In[49]:


def evenorodd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num=8
evenorodd(num)
    


# 14. If-Elif-else

# In[41]:


def marks(marks):
    if marks<25 and marks<=50:
        print("C Grade")
    elif marks>50 and marks<=85:
        print("B Grade")
    elif marks>85 and marks<=100:
        print("A Grade")
    else:
        print("Fail")
m= 88
marks(m)


# 15.Nested If

# In[48]:


def func(username,password):
    if username.strip() == "" or password.strip() == "":
        print("Invalid.Empty Inputs")
    else:
        if username == "admin":
            if password == "pass123":
                print("Valid.Login Successful!")
            else:
                print("Invalid")
        else:
            print("Invalid")
user=input("Enter username:")
pwd=input("Enter password:")
func(user,pwd)


# 16. For Loop Basics

# In[2]:


def num(count):
    if count<=0:
        print("Invalid Input")
    else:
        for i in range(5):
            print(i,end=" ")
count=int(input())         
num(count)


# 17. While Loop

# In[5]:


def loop(count):
    if count<=0:
        print("Invalid Input")
    else:
        while count>0:
            print(count,end=" ")
            count-=1
            
n=int(input())
loop(n)

    


# 18. Break Statement

# In[8]:


def findeve(start,end):
    if start>=end:
        print("Invalid Input")
    else:
        for i in range(start,end+1):
            if i%2==0:
                print(i,"is the first even number for the given range")
                break
start=int(input("Enter the start of range:"))
end=int(input("Enter the end of the range:"))
findeve(start,end)
            
        
    


# 19. Continue Statement

# In[13]:


def addodd(n):
    if n<=0:
        print("")
    else:
        s=0
        for i in range(10):
                if i%2==0:
                    continue
                else:
                    s+=i
        print("The sum of all the Odd number of the given range is: ",s)
n=10
addodd(n)
                    


# 20. Pass Statement

# In[14]:


def p():
    pass
p()
print("Function Defined")


# 21. Consistent Indentation

# In[18]:


def func(a,b):
    if a>0:
        if b>a:
            print("Nested")
        else:
            print("Invalid")
    print("Function completed")
a=int(input())
b=int(input())
func(a,b)
            


# 22. Comment Usage

# In[22]:


#define the function totalsal with the parameters base,bonus
def totalsal(base,bonus):
    total=base+bonus #Calculate the total salary
    #by adding up base salary he recieves with the bonus amt
    print("Total Salary: Rs.{:.2f}".format(total))#Print the total salary
    
#Get the input values from the user to calculate totalsal()
base=float(input("Enter the base salary:"))
bonus=float(input("Enter the bonus amount recieved:"))
totalsal(base,bonus)
    


# 23. Important Standard Module

# In[26]:


import math as m
def areaofcircle(radius):
    area= m.pi * (radius*radius)
    print("Area of the Circle: {:.2f} m² ".format(area))
r=float(input("Enter the radius:"))
areaofcircle(r)
    
    


# 24. All Import

# In[39]:


import math
from math import *
def mathfunc(n):
    if not isinstance(n,(int,float)):
        print("Invalid Input")
    else:
        print("Square root function: ",int(math.sqrt(n)))
        print("Power function: ",int(math.pow(n,2)))
        print("Pi Function:",int(math.pi * math.pow(n,2)))
num=int(input("Enter number:"))
mathfunc(num)
    


# 25. Parameters

# In[42]:


def add(a,b):
    s=a+b
    return s
result=add(5,3)
print("Result:",result)


# 26. Multiple Parameters

# In[43]:


def area(length, width):
    if length <= 0 or width <= 0:
        return "Invalid Input"
    
    a = length * width
    return a

result = area(5, 3)
print("Area:", result)


# 27. Len Function

# In[46]:


def lengthof(st):
    print("The length of the given string:",len(st))
string=input("Enter a string:")
lengthof(string)


# 28. Write to File

# In[48]:


def write_file():
    file=open("file.txt","w")
    file.write("Hello World")
    file.close()
    print("File written successfully")
write_file()


# 29. Read from file

# In[51]:


def read_file():
        file = open("file.txt","r")
        content= file.read()
        print("Content inside file.txt:",content)
        file.close()
read_file()


# 30. Basic Try-Except

# In[52]:


def divide(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

divide(x, y)


# 31. Create List

# In[53]:


def cart_items():
    cart = [100, 250, 75]

    if len(cart) == 0:
        print("Cart is empty")
    else:
        print("Cart Items:", cart)

cart_items()


# 32. Append to List

# In[54]:


def add_expense(amount):
    expenses = [100, 250, 75]

    if amount <= 0:
        print("Invalid Expense Amount")
    else:
        expenses.append(amount)
        print("Updated Expenses List:", expenses)

amt = int(input("Enter expense amount: "))
add_expense(amt)


# 33. Update dictionary

# In[55]:


def update_data():
    emp1 = {"Name": "John", "Age": 25}
    emp2 = {"Salary": 30000, "City": "Chennai"}

    if len(emp1) == 0 or len(emp2) == 0:
        print("Invalid Dictionary")
    else:
        emp1.update(emp2)
        print("Updated Employee Data:", emp1)

update_data()


# 34. Nested Dictionary

# In[56]:


def get_salary(dept, emp):
    employees = {
        "IT": {
            "John": 50000,
            "David": 60000
        },
        "HR": {
            "Sara": 45000
        }
    }

    if dept in employees and emp in employees[dept]:
        print("Salary:", employees[dept][emp])
    else:
        print("Employee or Department not found")

get_salary("IT", "John")


# 35. Create Tuple

# In[57]:


def coordinates():
    point = (10, 20)

    if len(point) != 2:
        print("Invalid Coordinates")
    else:
        print("Coordinates:", point)

coordinates()


# 36. Set Intersection

# In[58]:


def common_skills():
    set1 = {"Python", "Java", "C++"}
    set2 = {"Python", "HTML", "Java"}

    if len(set1) == 0 or len(set2) == 0:
        print("Invalid Input")
    else:
        common = set1 & set2
        print("Common Skills:", common)

common_skills()


# 37. Multiple Instances

# In[59]:


class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)

e1 = Employee("John")
e2 = Employee("David")

e1.display()
e2.display()


# 38. Method chaining

# In[60]:


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


# 39. Polymorphism

# In[61]:


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


# 40. Class Methods

# In[62]:


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

emp = Employee.from_string("Shubh,75000")

emp.display()


# In[ ]:




