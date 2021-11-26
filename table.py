import pandas as pd
import time
import yfinance as yf

from flask import Flask

app = Flask(__name__)

@app.route('/')
def data_scraper():
    while True:
        btc_historical = yf.download("BTC-USD", period="1d", interval="1m")
        btc_historical = btc_historical.tail()
        return btc_historical.to_html(header="true", table_id="table")

        time.sleep(60)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)