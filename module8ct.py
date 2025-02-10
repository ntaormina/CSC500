class ShoppingCart:
    customer_name = "none"
    current_date = "January 1, 2020"
    cart_items = []
    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

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

def add_item(ItemToPurchase):
    cart.cart_items.append(ItemToPurchase)

def remove_item(ItemToRemove):
    i = 0
    for item in cart.cart_items:
        if ItemToRemove == cart.cart_items[i].item_name:
            del cart.cart_items[i]
            return
        else:
            i = i + 1
    print("Item not found in cart. Nothing removed.")



def modify_item(ItemToPurchase):
    i = 0
    for item in cart.cart_items:
        if ItemToPurchase == cart.cart_items[i].item_name and cart.cart_items[i].item_quantity != None and cart.cart_items[i].item_price != None:
            cart.cart_items[i].item_quantity = int(input("Enter a new item quantity: "))
            return
        else:
            i = i + 1
    print("Item not found in cart. Nothing modified.")

def get_num_items_in_cart():
    print("Number of items:",len(cart.cart_items))

def get_cost_of_cart(item_total=None):
    i = 0
    item_grand_total = 0
    for item in cart.cart_items:
        item_total = cart.cart_items[i].item_price * cart.cart_items[i].item_quantity
        item_grand_total += item_total
        i = i + 1
    print("total $", item_grand_total)

def print_total():
    if len(cart.cart_items) == 0:
        print("SHOPPING CART IS EMPTY")
    else:
        get_cost_of_cart()

def print_descriptions():
    print(cart.customer_name,"'s Shopping cart -", cart.current_date,"\nItem Descriptions")
    for item in cart.cart_items:
        print(item.item_name, ":", item.item_description)

def print_menu(ShoppingCart):
    print("MENU\na - Add item to cart\n r - Remove item from cart\n c - change item quantity\n i - output item descriptions\n o - output item quantity\n q - Quit")

cart = ShoppingCart(customer_name="Jane Doe", current_date="January 1, 2025")
cart.customer_name = input("Enter customer name: ")
cart.current_date = input("Enter today's date: ")
print("Customer name:", cart.customer_name)
print("Today's date:", cart.current_date)
print_menu(cart)

while True:
    choice = input("Choose an option:")
    if choice == "q":
        exit(0)
    elif choice == "a":
        item1 = ItemToPurchase("item1", 0, 0)
        item1.item_name = input("Enter the item name:")
        item1.item_price = float(input("Enter the item price:"))
        item1.item_description = input("Enter the item description:")
        item1.item_quantity = int(input("Enter the item quantity:"))
        add_item(item1)
    elif choice == "r":
        itemToRemove = input("Enter the item to remove:")
        remove_item(itemToRemove)
    elif choice == "c":
        itemToChange = input("Enter the item to change:")
        modify_item(itemToChange)
    elif choice == "i":
        print_descriptions()
    elif choice == "o":
        print(cart.customer_name, "'s Shopping cart -", cart.current_date)
        get_num_items_in_cart()
        for item in cart.cart_items:
            print_item_cost(item.item_name, item.item_quantity, item.item_price)
        print_total()
    

