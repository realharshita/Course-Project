def convert(from_currency, to_currency, amount, rates):
  if from_currency not in rates or to_currency not in rates:
    return None
  exchange_rate = rates[to_currency] / rates[from_currency]
  return amount * exchange_rate

rates = {
  "USD": 1.0,
  "EUR": 0.92,
  "GBP": 0.82,
  "JPY": 114.13,
  "INR": 83.4
}

from_currency = input("Enter from currency (e.g., USD, EUR): ").upper()
to_currency = input("Enter to currency (e.g., USD, EUR): ").upper()
amount = float(input("Enter amount: "))

converted_amount = convert(from_currency, to_currency, amount, rates)

if converted_amount is not None:
  print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
  print("Invalid currency code")
