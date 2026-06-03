class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [i for i in self.items if i.name != name]

    def calculate_total(self):
        return sum(i.price * i.quantity for i in self.items)

def main():
    cart = ShoppingCart()
    cart.add_item(CartItem("Laptop", 1000, 1))
    cart.add_item(CartItem("Mouse", 20, 2))
    total = cart.calculate_total()
    gst = total * 0.18
    print(f"Total: {total}\nGST (18%): {gst:.2f}\nFinal Receipt: {total + gst:.2f}")

if __name__ == "__main__":
    main()
