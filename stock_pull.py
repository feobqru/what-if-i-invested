import yfinance as yf
from datetime import datetime
import json
import os

start_date = input("When did you buy your phone? (YYYY-MM-DD): ")
end_date = datetime.today().strftime('%Y-%m-%d')
purchase_price = float(input("What was the price of your phone? (in USD): "))

stock_data = yf.download("AAPL", start=start_date, end=end_date)
prices=stock_data['Close']
initial_price = prices.iloc[0]
shares_owned = purchase_price / initial_price
stock_data['predicted_value'] = prices * shares_owned

data = {
    "dates": stock_data.index.strftime('%Y-%m-%d').tolist(),
    "values": stock_data['predicted_value'].tolist(),
    "purchase_price": purchase_price
}

with open("chart_data.json", "w") as f:
    json.dump(data, f)
