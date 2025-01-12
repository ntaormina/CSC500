def print_item_cost(item_name, item_quantity, item_price):
    print(item_name,item_quantity," @ $",item_price," = $",float(item_price * item_quantity))


class ItemToPurchase:
    item_name = "none"
    item_price: float = 0.00
    item_quantity: int = 0
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity


item1 = ItemToPurchase("item1", 0, 0)
item2 = ItemToPurchase("item2", 0, 0)

item1.item_name = input("Enter the item name:")
item1.item_price = float(input("Enter the item price:"))
item1.item_quantity = int(input("Enter the item quantity:"))
item2.item_name = input("Enter the item name:")
item2.item_price = float(input("Enter the item price:"))
item2.item_quantity = int(input("Enter the item quantity:"))

print("TOTAL COST")
print_item_cost(item1.item_name, item1.item_quantity, item1.item_price)
print_item_cost(item2.item_name, item2.item_quantity, item2.item_price)

print("Total = $",(item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity))
