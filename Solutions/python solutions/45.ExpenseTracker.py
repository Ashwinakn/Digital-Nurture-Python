import csv
from datetime import datetime

def main():
    with open('expenses.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Amount', 'Category'])
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), '50', 'Food'])
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), '100', 'Transport'])

    current_month = datetime.now().month
    current_year = datetime.now().year
    
    category_totals = {}
    with open('expenses.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date_obj = datetime.strptime(row['Date'], "%Y-%m-%d")
            if date_obj.month == current_month and date_obj.year == current_year:
                category = row['Category']
                amount = float(row['Amount'])
                category_totals[category] = category_totals.get(category, 0) + amount

    print("Current Month Expense Summary:")
    for cat, total in category_totals.items():
        print(f"{cat}: {total:.2f}")

if __name__ == "__main__":
    main()
