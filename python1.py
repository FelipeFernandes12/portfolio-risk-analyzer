"""historical_prices = [95.00, 102.50, 98.10, 105.00, 112.30, 89.90]

for price in historical_prices:
    if price > 100.00:
        print(f"Price {price:.2f} Target broken! ")
    else:
        print(f"Price {price:.2f} Below target. ")"""

"""monthly_sales = [4500, 12000, 8000, 15000, 3000, 22000]
high_value_sales = []  # Start with this empty list
max_sale = max(monthly_sales)
for sale in monthly_sales:
    if sale == max_sale:
        high_value_sales.append(sale)
print(f"High-value sales: {high_value_sales}")

transactions = [100, 250, 50, 1200, 400]

total_volume = 0   # Accumulator variable for volume
total_tax = 0      # Accumulator variable for tax

for transaction in transactions:
    total_volume += transaction  # Add the transaction amount to total volume
    tax = transaction * 0.10     # Calculate tax as 10% of the transaction
    total_tax += tax            # Add the tax to total tax

print(f"Total Volume: ${total_volume:.2f}")
print(f"Total Tax: ${total_tax:.2f}")"""

user_ids = [5022, 1009, 9054, "TEST_ID", 3341]
#Use remove() to delete the string "TEST_ID" from the list
user_ids.remove("TEST_ID")
#User .sort() to sort the list in ascending order
user_ids.sort()
print(f"Sorted User IDs: {user_ids}")