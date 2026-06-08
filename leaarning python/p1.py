"""apple = "Red"
banana = "Yellow"
basket = apple
apple = banana
banana = basket"""

"""apple = "Red"
banana = "Yellow"

# The Python Shortcut Swap:
apple, banana = banana, apple

print("Apple:", apple)
print("Banana:", banana)

product_price = 80.00
increase = 0.15
product_new_price = product_price * (1 + increase)
print("The new price is:", product_new_price)"""

"""# Rewrite this using () line continuation:
projected_yearly_revenue = (current_revenue * inflation_rate + new_product_sales 
- operating_costs - marketing_spend
 + government_subsidies)"""


"""sql_query = "SELECT user_id, transaction_date, item_name, " \
"total_price FROM ecommerce_sales_table WHERE total_price > 500.00 " \
"AND country = 'Brazil' ORDER BY transaction_date DESC;"""

"""transaction_amount = 5000.00
is_vip_customer = False

if transaction_amount > 1000.00:
    fee_percentage = 0.02
print("Applying standard high-volume fee.")
if is_vip_customer:
    fee_percentage = 0.01
print("VIP discount applied!")
    
final_fee = transaction_amount * fee_percentage
print(f"The final processing fee is: R$ {final_fee:.2f}")"""

"""database_id = "ID-9945"
number = database_id[3]
print(f"The character at index 3 of the database ID is: '{number}'")"""

"""stock_data = "2026-06-05_TICKER:AAPL_PRICE:175.50"
ticker = stock_data[18:22]
print(f"The ticker symbol extracted from the stock data is: '{ticker}'")"""

"""current_stock_price = 154.50
buy_alert_threshold = 150.00
sell_alert_threshold = 200.00

if current_stock_price <= buy_alert_threshold:
    print("Buy Alert: The stock price is at or below the buy threshold.")
elif current_stock_price >= sell_alert_threshold:
    print("Sell Alert: The stock price is at or above the sell threshold.")
else:
    print("Hold: The stock is between the buy and sell thresholds.")"""

"""transaction_amount = 8500.00
is_recognized_device = False
location = "Russia"""

"""if transaction_amount > 5000.00 and location == "Russia":
    print("High-risk transaction detected: Large amount from Russia.")"""

"""if is_recognized_device == True or transaction_amount <= 1000.00:
    print("Transaction is from a recognized device or not from Russia.")"""

"""account_status = "Active"
purchase_amount = 12500.00

# Write your if / elif / else logic below:

if account_status == "Active":
    if purchase_amount > 10000.00:
        print("High-value purchase detected for an active account.")
    else:
        print("Transaction approved.")
else:
    print("Transaction approved")

def clean_and_convert(value,exchange_rate):
    cleaned_value = value.replace("$", "").replace(",", "")
    numeric_value = float(cleaned_value)
    converted_value = numeric_value * exchange_rate
    return converted_value

# Example usage:
value = "$1,234.56"
exchange_rate = 0.18
result = clean_and_convert(value, exchange_rate)
print(f"The converted value is: {result:.2f}")"""

name = "Fe" + "lip" + "e"
print(f"The name is: {name}")
