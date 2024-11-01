from Colors import bcolors

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item, quantity=1):
        # If item exists, increase quantity; otherwise, add new item
        for inv_item in self.inventory:
            if inv_item.name == item.name:
                inv_item.quantity += quantity
                return
        item.quantity = quantity
        self.inventory.append(item)

    def remove_item(self, item):
        # Remove item if its quantity is less than or equal to zero
        if item in self.inventory:
            if item.quantity > 1:
                item.quantity -= 1
            else:
                self.inventory.remove(item)
            return True
        else:
            return False

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        for item in self.inventory:
            print(f"{item.name} | Quantity: {item.quantity} | Description: {item.description}")

