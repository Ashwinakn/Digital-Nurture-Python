def update_data():
    emp1 = {"Name": "John", "Age": 25}
    emp2 = {"Salary": 30000, "City": "Chennai"}

    if len(emp1) == 0 or len(emp2) == 0:
        print("Invalid Dictionary")
    else:
        emp1.update(emp2)
        print("Updated Employee Data:", emp1)

update_data()
