class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print(f"ALERT: {self.name} budget exceeded!")

def main():
    budget = {
        "Food": Category("Food", 500),
        "Rent": Category("Rent", 1000)
    }
    
    budget["Food"].add_expense(200)
    budget["Food"].add_expense(400)
    
    print("Budget Summary:")
    for cat in budget.values():
        print(f"{cat.name}: Spent {cat.spent}/{cat.limit}")

if __name__ == "__main__":
    main()
