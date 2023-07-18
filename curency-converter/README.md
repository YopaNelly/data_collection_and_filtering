# curency converter

Task: Currency Converter
Stage 1: Input Collection

Prompt the user to enter an amount in a specific currency.
Prompt the user to enter the currency code of the input amount (e.g., USD, EUR).
Stage 2: Conversion Function

Write a function called convert_currency that takes two arguments: the amount and the currency code.
Inside the function, define a dictionary that maps currency codes to conversion rates.
Check if the given currency code exists in the dictionary. If not, return an error message.
If the currency code is valid, calculate the converted amount by multiplying the input amount with the corresponding conversion rate.
Return the converted amount from the function.
Stage 3: Function Invocation and Output

Call the convert_currency function, passing the user input amount and currency code as arguments.
Store the returned converted amount in a variable.
Print the original amount and the converted amount with the currency symbol as the output.