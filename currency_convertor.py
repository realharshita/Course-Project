import requests

# API endpoint with your access key (replace with your own)
api_url = "https://api.exchangerate-api.com/v4/latest?base="

def get_rate(from_currency, to_currency):
  response = requests.get(api_url + from_currency)
  data = response.json()
  if data["success"]:
    return data["rates"][to_currency]
  else:
    return None

def convert():
  while True:
    from_currency = input("Enter from currency (e.g., USD, EUR): ").upper()
    to_currency = input("Enter to currency (e.g., USD, EUR): ").upper()
    amount = input("Enter amount: ")
    try:
      amount = float(amount)
      break
    except ValueError:
      print("Invalid amount. Please enter a number.")
  
  rate = get_rate(from_currency, to_currency)
  if rate:
    converted_amount = amount * rate
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
  else:
    print("Invalid currency code")

if __name__ == "__main__":
  print("Welcome to Currency Converter!")
  convert()
  print("\nWould you like to convert again? (y/n)")
  choice = input().lower()
  while choice == 'y':
    convert()
    print("\nWould you like to convert again? (y/n)")
    choice = input().lower()
  print("Thank you for using Currency Converter!")
