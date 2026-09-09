# This program calculates the total cost based on item price and quantity

# Ask the user for inputs
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity you want: ")

# Convert inputs to the correct data types
price = float(price_input)   # Price can be a decimal (e.g., 49.99)
quantity = int(quantity_input)   # Quantity must be a whole number

# Calculate the total
total = price * quantity

# Print a friendly summary using an f-string with 2-decimal formatting
print(f"{quantity} items at {price:.2f} each = {total:.2f}")