from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf

app = Flask(__name__)

# Login page route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print ("Inside Login")
        username = request.form.get('username')
        password = request.form.get('password')
        # Add your login validation here (simple example)
        if username == "admin" and password == "password":
            print ("Checking Username and password")
            return redirect(url_for('dashboard'))
        else:
            print ("Login failed Invalid User")
            return render_template('front.html', error="Invalid credentials")
    print ("If condition didnot Hit hence returing the front.html")
    return render_template('front.html')

# Dashboard (stock fetcher) route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    stock_data = None
    error = None

    if request.method == 'POST':
        ticker = request.form.get('ticker')
        start_date = request.form.get('start')
        end_date = request.form.get('end')

        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if data.empty:
                error = "No data found. Please check the ticker symbol and dates."
            else:
                stock_data = data.to_html(classes='table table-striped')
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', stock_data=stock_data, error=error)

if __name__ == '__main__':
    print ("App starts");
    app.run(debug=True)
