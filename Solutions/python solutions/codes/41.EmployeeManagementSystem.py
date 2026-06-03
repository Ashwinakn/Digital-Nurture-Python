import json

class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}"

def main():
    employees = {
        "1": Employee("1", "Alice", "HR"),
        "2": Employee("2", "Bob", "IT")
    }

    with open('emps.json', 'w') as f:
        json_data = {k: {"emp_id": v.emp_id, "name": v.name, "department": v.department} for k, v in employees.items()}
        json.dump(json_data, f)

    loaded_employees = {}
    with open('emps.json', 'r') as f:
        data = json.load(f)
        for k, v in data.items():
            loaded_employees[k] = Employee(v["emp_id"], v["name"], v["department"])

    for emp in loaded_employees.values():
        print(emp)

if __name__ == "__main__":
    main()
