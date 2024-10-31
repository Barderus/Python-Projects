class Inventory():
    def __init__(self):
        self.inventory = []

    def add_item(self, item, quantity):

        if item in self.inventory:
            item.quantity += 1
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            return False

    def check_item(self, item):
        if item in self.inventory and item.quantity > 0:
            item.quantity -= 1
            if item.quantity <= 0:
                self.remove_item(item)
            return True
        else:
            return False


    def view_inventory(self, inventory):
        for item in inventory:
            print(f"{item.name} | {item.quantity} | {item.description}")