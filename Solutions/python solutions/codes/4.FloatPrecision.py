def flprecision(salary,tax_rate):
    if not isinstance(salary,float) and not isinstance(tax_rate,float):
        print("Invalid Input")
    else:
        netsalary = salary * (1-tax_rate)
        print("Net Salary = {:.2f}".format(netsalary))
salary=75000.5
tax_rate=0.18
flprecision(salary,tax_rate)
