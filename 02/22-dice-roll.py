import random

computers_throw = random.randrange(1, 7)

users_guess = int(input('Enter your guess: '))

print(computers_throw == users_guess)