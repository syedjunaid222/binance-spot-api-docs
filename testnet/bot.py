from flask import Flask, request
from binance.client import Client
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

client = Client(API_KEY, API_SECRET)
client.API_URL = 'https://testnet.binance.vision/api'

symbol = "XRPUSDT"
quantity = 100

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", "")

    if "BUY SIGNAL" in message:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print("BUY order placed:", order)

    elif "SELL SIGNAL" in message:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print("SELL order placed:", order)

    return {"status": "success"}

if __name__ == '__main__':
    app.run()
