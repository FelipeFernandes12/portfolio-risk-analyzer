def process_transaction(amount):
    if amount > 3000:
        return region_rules["GLOBAL"]
    elif amount > 1000:
        return region_rules["EU"]
    else:
        return region_rules["US"]

# Raw transaction amounts (The last one is an internal system test string)
raw_transactions = [1200.00, 450.00, 3100.00, 890.00, 5000.00, 150.00, "SYSTEM_TEST"]

# Regional metadata profile
region_rules = {
    "US": 0.08,    # 8% tax
    "EU": 0.15,    # 15% tax
    "GLOBAL": 0.20 # 20% tax
}

raw_transactions.remove("SYSTEM_TEST")

index = 0
while index < len(raw_transactions):
    amount = raw_transactions[index]
    tax_rate = process_transaction(amount)
    tax_amount = amount * tax_rate
    print(f"Transaction amount: {amount:.2f}, Tax Rate: {tax_rate*100:.1f}%, Tax Amount: {tax_amount:.2f}")
    index += 1

