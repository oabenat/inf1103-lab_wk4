import json


def load_inventory():
    """Load the saved inventory total and transaction history."""
    try:
        with open("inventory.txt", "r", encoding="utf-8") as inventory_file:
            saved_data = json.load(inventory_file)
    except FileNotFoundError:
        return 0, []

    return saved_data["total"], saved_data["history"]


def save_inventory(total, history):
    """Save the inventory total and transaction history."""
    saved_data = {"total": total, "history": history}
    with open("inventory.txt", "w", encoding="utf-8") as inventory_file:
        json.dump(saved_data, inventory_file, indent=2)


failed_entries = 0


def get_valid_input():
    """Prompt until the user enters a non-negative integer or quit."""
    global failed_entries

    while True:
        entry = input("Enter stock quantity or 'quit': ").strip()

        if entry.lower() == "quit":
            return "quit"

        if entry.startswith("-") and entry[1:].isdigit():
            print("Error: stock quantity cannot be negative.")
            failed_entries += 1
            continue

        if entry.isdigit():
            return int(entry)

        print("Error: enter a whole number or 'quit'.")
        failed_entries += 1


def process_delivery(current_total, new_value):
    """Add one delivery to the running inventory total."""
    return current_total + new_value


def calculate_tax(amount):
    """Return 10 percent tax for one delivery."""
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    """Print the final processing summary."""
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


inventory, transaction_history = load_inventory()
deliveries_processed = 0
total_tax = 0

while True:
    delivery = get_valid_input()

    if delivery == "quit":
        save_inventory(inventory, transaction_history)
        generate_report(deliveries_processed, failed_entries)
        break

    inventory = process_delivery(inventory, delivery)
    transaction_history.append(delivery)
    total_tax += calculate_tax(delivery)
    deliveries_processed += 1
