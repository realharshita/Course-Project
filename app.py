# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded exchange rates (example rates, not actual)
exchange_rates = {
    'USD': {'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'JPY': 129.0, 'GBP': 0.88},
    'JPY': {'USD': 0.0091, 'EUR': 0.0078, 'GBP': 0.0069},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 144.0}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])
        
        # Calculate the conversion
        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            rate = exchange_rates[from_currency][to_currency]
            result = amount * rate
        else:
            result = "Conversion rate not available"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
