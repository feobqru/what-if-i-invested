import yfinance as yf
from datetime import datetime
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/get_chart_data')
def get_chart_data():
    with open("chart_data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit-form', methods=["POST"])
def handle_form():
    date_received = request.form.get("date")
    phone_received = float(request.form.get("phones"))
    start_date = date_received
    end_date = datetime.today().strftime('%Y-%m-%d')
    purchase_price = phone_received

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
    return render_template("graph_page.html")

if __name__ == '__main__':
    app.run(debug=True)