# This program calculates the total cost based on item price and quantity
# It includes error handling to prevent crashes from invalid input

# Get valid price from user (allows decimals)
while True:
    price_input = input("Enter the price of one item: ")
    try:
        price = float(price_input)
        break  # Exit loop if conversion succeeds
    except ValueError:
        print("Invalid input. Please enter a valid number for the price (e.g., 49.99).")

# Get valid quantity from user (must be a whole number)
while True:
    quantity_input = input("Enter the quantity you want: ")
    try:
        quantity = int(quantity_input)
        if quantity < 0:
            print("Quantity cannot be negative. Please enter a positive whole number.")
            continue  # Ask again if negative
        break
    except ValueError:
        print("Invalid input. Please enter a whole number for the quantity (e.g., 3).")

# Calculate the total
total = price * quantity

# Print a friendly summary using an f-string with 2-decimal formatting
print(f"{quantity} items at {price:.2f} each = {total:.2f}")