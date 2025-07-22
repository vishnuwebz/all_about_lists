# Inventory Management System
import random

# Initialize inventory as a list of dictionaries
inventory = [
    {"id": 1, "name": "Laptop", "price": 50000, "quantity": 10},
    {"id": 2, "name": "Phone", "price": 20000, "quantity": 20}
]

# Function to add item
def add_item(id, name, price, quantity):
    inventory.append({"id": id, "name": name, "price": price, "quantity": quantity})
    print(f"Added {name} to inventory")

# Function to remove item
def remove_item(id):
    for item in inventory:
        if item["id"] == id:
            inventory.remove(item)
            print(f"Removed {item['name']}")
            return
    print("Item not found")

# Function to apply random discount
def apply_discount():
    for item in inventory:
        discount = random.randint(5, 20)  # Random 5-20% discount
        item["price"] *= (1 - discount / 100)
        print(f"Applied {discount}% discount to {item['name']}: New Price ₹{item['price']:.2f}")

# Function to display inventory
def display_inventory():
    print("\nInventory:")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ₹{item['price']:.2f}, Quantity: {item['quantity']}")

# Main program
print("Welcome to Inventory Manager")
while True:
    action = input("Enter action (add/remove/discount/display/exit): ").lower()
    if action == "add":
        id = int(input("Enter ID: "))
        name = input("Enter item name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        add_item(id, name, price, quantity)
    elif action == "remove":
        id = int(input("Enter ID to remove: "))
        remove_item(id)
    elif action == "discount":
        apply_discount()
    elif action == "display":
        display_inventory()
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid action")
# Example run:
# Input: add, 3, Tablet, 15000, 15
# Output: Added Tablet to inventory
# Input: discount
# Output: Applied 10% discount to Laptop: New Price ₹45000.00
#         Applied 15% discount to Phone: New Price ₹17000.00
#         Applied 12% discount to Tablet: New Price ₹13200.00
# Input: display
# Output: Inventory:
#         ID: 1, Name: Laptop, Price: ₹45000.00, Quantity: 10
#         ID: 2, Name: Phone, Price: ₹17000.00, Quantity: 20
#         ID: 3, Name: Tablet, Price: ₹13200.00, Quantity: 15