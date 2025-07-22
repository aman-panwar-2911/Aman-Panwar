from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf

app = Flask(__name__)

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple check
        if username == "admin" and password == "password":
            return redirect(url_for('dashboard'))
        else:
            return render_template('front.html', error="Invalid credentials")
    return render_template('front.html')

# Dashboard route
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

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"New user signup: {username}")
        return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
