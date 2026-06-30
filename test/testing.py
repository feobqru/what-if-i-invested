import yfinance as yf
import matplotlib.pyplot as plt


start_date = input("When did you buy your phone? (YYYY-MM-DD): ")
stock_data = yf.download("AAPL", start=start_date, end="2026-01-01")
stock_data.head() 


plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Closing Price', color='blue')
plt.title("Apple Stock Closing Prices (2022)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()

start_date = input("When did you buy your phone? (YYYY-MM-DD): ")

