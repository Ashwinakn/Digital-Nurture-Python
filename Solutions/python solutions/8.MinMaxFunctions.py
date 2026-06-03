def findminmax(list):
    salary=[]
    for i in list:
        if isinstance(i,(int,float)):
            salary.append(i)
    print(min(salary))
    print(max(salary))
s=[50000,75000,62000,95000]
findminmax(s)
