pom = int(input('Enter the amount in PLN: '))
amount = pom

fives = amount // 5
amount //= 5

twoes = amount // 2
amount //= 2

ones = amount

print(
    f"The amount of PLN {pom} in coins: \n 5 zł - {fives} \n 2 zł - {twoes} \n 1 zł - {ones}")