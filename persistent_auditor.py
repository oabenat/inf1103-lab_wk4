import json


DEFAULT_ORDERS = [
    {"id": 1001, "product": "Wireless Mouse", "quantity": 2},
    {"id": 1002, "product": "Keyboard", "quantity": 1},
    {"id": 1003, "product": "USB Cable", "quantity": 3},
]


def load_orders():
    """Load saved orders or return the initial order list."""
    try:
        with open("orders.txt", "r", encoding="utf-8") as orders_file:
            return json.load(orders_file)
    except FileNotFoundError:
        return DEFAULT_ORDERS.copy()


def save_orders(orders):
    """Save all orders to orders.txt."""
    with open("orders.txt", "w", encoding="utf-8") as orders_file:
        json.dump(orders, orders_file, indent=2)


def display_orders(orders):
    """Display each order in the required comma-separated format."""
    print("Current Orders:")
    print()
    for order in orders:
        print(f"{order['id']}, {order['product']}, {order['quantity']}")
    print()


def get_quantity():
    """Prompt until the user enters a positive whole-number quantity."""
    while True:
        entry = input("Enter Quantity: ").strip()
        if entry.isdigit() and int(entry) > 0:
            return int(entry)
        print("Error: quantity must be a positive whole number.")


orders = load_orders()
display_orders(orders)

product = input("Enter Product Name: ").strip()
quantity = get_quantity()
new_order = {
    "id": orders[-1]["id"] + 1,
    "product": product,
    "quantity": quantity,
}
orders.append(new_order)

print()
print("New Order Added:")
print(f"{new_order['id']}, {new_order['product']}, {new_order['quantity']}")
save_orders(orders)
print()
print("Order successfully saved to orders.txt")