def currency_converter(amount, from_currency, to_currency):
    currencies = {
        "USD": 1.0,
        "EUR": 0.87,
        "GBP": 0.78,
        "INR": 76.69,
        "TK": 105.65,
        "CNY": 6.49
    }
    converted_amount = amount * (currencies[to_currency] / currencies[from_currency])
    return converted_amount

if __name__ == "__main__":
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (USD, EUR, GBP, INR, TK, CNY): ")
    to_currency = input("Enter the currency to convert to (USD, EUR, GBP, INR, TK, CNY): ")
    
    converted_amount = currency_converter(amount, from_currency, to_currency)
    print("Converted amount: ", converted_amount)
