"""system_config = (2026, "Production")
print(f"{system_config}")
print(f"The configuration is {system_config[1]}")"""

asset_data = {
    "ticker": "TSLA",
    "price": 180.50,
    "volume": 45000
}
"""Write a print statement that
uses the key to pull out and print just the price of the asset. # type: ignore"""
asset_data["price"] = 180.00
print(f"The price of {asset_data['ticker']} is ${asset_data['price']:.2f} and the volume is{asset_data['volume']}")