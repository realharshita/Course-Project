from flask import Flask, render_template, request

app = Flask(__name__)

# Exchange rates relative to USD
exchange_rates_to_usd = {
    'USD': 1.0,
    'EUR': 0.85,  # Euro
    'JPY': 110.0,  # Japanese Yen
    'GBP': 0.75,  # British Pound
    'AUD': 1.3,   # Australian Dollar
    'CAD': 1.25,  # Canadian Dollar
    'CHF': 0.92,  # Swiss Franc
    'CNY': 6.47,  # Chinese Yuan Renminbi
    'SEK': 8.6,   # Swedish Krona
    'NZD': 1.4,   # New Zealand Dollar
    'BRL': 5.20,  # Brazilian Real
    'MXN': 20.0,  # Mexican Peso 
    'INR': 78.0,  # Indian Rupee 
    'KRW': 1200.0,  # South Korean Won 
    'THB': 34.0,  # Thai Baht 
    'IDR': 14000.0,  # Indonesian Rupiah 
    'ZAR': 17.0,  # South African Rand 
    'TRY': 17.5,  # Turkish Lira 
    'AED': 3.67,  # United Arab Emirates Dirham
    'SGD': 1.35   # Singapore Dollar 
}

# Inverse the exchange rates for convenience
exchange_rates_from_usd = {currency: 1 / rate for currency, rate in exchange_rates_to_usd.items()}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    currencies = list(exchange_rates_to_usd.keys())
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']
        
        if not amount:
            result = "Invalid input. Please enter a valid number."
        else:
            try:
                amount = float(amount)
                # Convert from source currency to USD first, then to target currency
                if from_currency in exchange_rates_to_usd and to_currency in exchange_rates_from_usd:
                    amount_in_usd = amount / exchange_rates_to_usd[from_currency]
                    result = f"{amount} {from_currency} = {amount_in_usd * exchange_rates_from_usd[to_currency]:.2f} {to_currency}"
                else:
                    result = "Conversion rate not available"
            except ValueError:
                result = "Invalid input. Please enter a valid number."

    return render_template('index.html', currencies=currencies, result=result)

if __name__ == '__main__':
    app.run(debug=True)
