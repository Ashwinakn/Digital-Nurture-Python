import csv

def main():
    with open('employees.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Salary'])
        writer.writerow(['Alice', '45000'])
        writer.writerow(['Bob', '60000'])
        writer.writerow(['Charlie', '70000'])

    with open('employees.csv', 'r') as f:
        reader = csv.DictReader(f)
        employees = [row for row in reader]

    high_earners = [float(emp['Salary']) for emp in employees if float(emp['Salary']) > 50000]
    
    if high_earners:
        avg_salary = sum(high_earners) / len(high_earners)
        print(f"Average salary for employees earning > 50000: {avg_salary:.2f}")
    else:
        print("No employees earn more than 50000.")

if __name__ == "__main__":
    main()
