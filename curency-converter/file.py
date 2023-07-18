#  Currency Converter

# stage 1
amount = int(input("Enter an amount in a specific currency:"))
 
code = input("Enter the currency code of the input amount (e.g., USD, EUR, GBP, JPY): ")

#Stage 2

def convert_currency(amount, codeS):

# define a dictionary that maps currency codes to conversion rates.

    my_dict = {
        "USD": 0.82,
        "EUR": 1.0,
        "GBP": 1.12,
        "JPY": 0.0076,
    }
    for i in my_dict:
        # Check if the given currency code exists in the dictionary
        if codeS not in my_dict:
            return "CURRENCY CODE not found"
        else:
            # multiplying the input amount with the corresponding conversion rate.

            converted_amout = amount * my_dict[codeS]

            return converted_amout
        

converted_amout = convert_currency(amount, code)

print("Original amount:  ", amount)
print("Converted amount: ", converted_amout, code)
