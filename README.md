# Currency Converter

This is a simple command line application that converts an amount from one currency to another. It uses the ExchangeRate-API to get real-time conversion rates.

## Installation

1. Clone this repository to your local machine.

   ```
   git clone https://github.com/yourusername/CurrencyConverter.git
   ```

2. Navigate into the project directory.

   ```
   cd CurrencyConverter
   ```

3. Install the required Python libraries.

   ```
   pip install -r requirements.txt
   ```

## Setup

1. Sign up on [ExchangeRate-API](https://www.exchangerate-api.com/) to get your API key.

2. Create a `.env` file in the project's root directory and add your API key to it:

   ```
   EXCHANGE_RATE_API_KEY=your_api_key
   ```

   Replace `your_api_key` with your actual API key.

## Usage

Run the script with Python:

```
python main.py
```

You will be prompted to enter:

- The currency you want to convert from (e.g., 'USD')
- The currency you want to convert to (e.g., 'EUR')
- The amount you want to convert

The script will then display the converted amount.

## Notes

- Currency codes should be entered as per the ISO 4217 standard (e.g., 'USD' for US Dollar, 'EUR' for Euro).
- Not all currencies may be supported, especially with the free version of ExchangeRate-API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
