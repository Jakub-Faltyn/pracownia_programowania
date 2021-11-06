correct_pin = '0805'
correct = False

for i in range(3):
    pin = input('Enter the PIN code: ')
    if pin == correct_pin:
        correct = True
        break
    elif i != 2:
        print("Incorrect...")

if not correct:
    print("Sorry, your payment card has been blocked.")
else:
    print("PIN is correct")