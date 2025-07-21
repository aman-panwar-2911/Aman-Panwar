from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        start = request.form['start']
        end = request.form['end']

        try:
            data = yf.download(ticker, start=start, end=end)
            if data.empty:
                return "<p>No data found. Please check the ticker symbol and dates.</p>"
            return f"<h2>Stock Data for {ticker}</h2><pre>{data.to_string()}</pre>"
        except Exception as e:
            return f"<p>Error: {e}</p>"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
