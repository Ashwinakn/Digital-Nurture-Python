class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

class Perishable(Product):
    pass

class Electronics(Product):
    pass

def main():
    inventory = {
        "Milk": Perishable("Milk", 5),
        "Laptop": Electronics("Laptop", 20)
    }

    low_stock = {
        name for name, product in inventory.items()
        if product.stock < 10
    }

    print("Inventory Summary")

    for name, product in inventory.items():
        print(name, "-", product.stock)

    print("Low Stock Alerts:", low_stock)

if __name__ == "__main__":
    main()
