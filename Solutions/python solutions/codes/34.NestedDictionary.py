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
