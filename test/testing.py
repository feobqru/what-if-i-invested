import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

start_date = input("When did you buy your phone? (YYYY-MM-DD): ")
end_date = datetime.today().strftime('%Y-%m-%d')

purchase_price = float(input("What was the price of your phone? (in USD): "))

stock_data = yf.download("AAPL", start=start_date, end=end_date)
stock_data.head() 
prices=stock_data['Close']

initial_price = prices.iloc[0]
shares_owned = purchase_price / initial_price
stock_data['predicted_value'] = prices * shares_owned

print(f"Shares owned: {shares_owned}")

plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['predicted_value'], color='blue')
plt.title("Apple Stock Closing Prices")
plt.axhline(purchase_price, color='red', linestyle=':', label=f'Initial ${purchase_price:.2f} Principal')
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()


