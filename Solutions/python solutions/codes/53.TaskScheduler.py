from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

def main():
    tasks = [
        Task("Submit Assignment", "2026-10-15", 1),
        Task("Pay Bills", "2026-08-01", 2),
        Task("Buy Groceries", "2026-01-01", 3)
    ]
    
    tasks.sort(key=lambda t: t.due_date)
    now = datetime.now()
    
    print("Sorted Task Schedule:")
    for t in tasks:
        status = "OVERDUE" if t.due_date < now else "Upcoming"
        print(f"{t.name} (Due: {t.due_date.strftime('%Y-%m-%d')}) - {status}")

if __name__ == "__main__":
    main()
