# Raw incoming data stream (Simulating a messy API response)
raw_portfolio = [
    {"ticker": "AAPL", "type": "Stock", "price": 175.50, "volatility": 0.12},
    {"ticker": "TSLA", "type": "Stock", "price": 180.20, "volatility": 0.45},
    {"ticker": "BTC", "type": "Crypto", "price": 65000.00, "volatility": 0.78},
    "CORRUPTED_LINE_ENTRY",  # Messy data to clean
    {"ticker": "GOOG", "type": "Stock", "price": 150.00, "volatility": 0.08},
    {"ticker": "ETH", "type": "Crypto", "price": 3500.00, "volatility": 0.62},
]

# Strict institutional thresholds
RISK_MULTIPLIERS = {
    "Stock": 1.5,
    "Crypto": 3.0
}

cleaned_portfolio = []
index = 0
while index < len(raw_portfolio):
    if isinstance(raw_portfolio[index], dict):
        cleaned_portfolio.append(raw_portfolio[index])
    elif isinstance(raw_portfolio[index], str):
        print(f"Warning: Skipping corrupted entry at index {index}. Data: {raw_portfolio[index]}")
    index += 1

def calculate_risk_score(asset_dict):
    asset_type = asset_dict["type"]
    volatility = asset_dict["volatility"]
    multiplier = RISK_MULTIPLIERS.get(asset_type, 1)
    return volatility * multiplier

for asset in cleaned_portfolio:
    risk_score = calculate_risk_score(asset)
    if risk_score > 1.5:
        print(f"High Risk Alert: {asset['ticker']} has a risk score of {risk_score:.2f}.")
    elif risk_score > 0.5:
        print(f"Moderate Risk: {asset['ticker']} has a risk score of {risk_score:.2f}.")
    else:
        print(f"Low Risk: {asset['ticker']} has a risk score of {risk_score:.2f}.")