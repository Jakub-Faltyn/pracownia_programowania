import math

VAT = 0.23

amount = float(input('Enter amount: '))
vat = "{:.2f}".format(amount * VAT)
print(f'VAT 23% : {vat} zł')