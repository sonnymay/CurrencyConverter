import requests
from dotenv import load_dotenv
import os

def get_conversion_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data['result'] == 'success':
        conversion_rate = data['conversion_rates'].get(to_currency)
        if conversion_rate:
            return conversion_rate
        else:
            print(f"Could not find conversion rate for {to_currency}")
            return None
    else:
        print("Failed to retrieve conversion rate")
        return None

def convert_currency(amount, conversion_rate):
    return amount * conversion_rate

def main():
    load_dotenv()
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    amount = float(input("Enter the amount you want to convert: "))
    conversion_rate = get_conversion_rate(from_currency, to_currency, api_key)
    if conversion_rate is not None:
        converted_amount = convert_currency(amount, conversion_rate)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
