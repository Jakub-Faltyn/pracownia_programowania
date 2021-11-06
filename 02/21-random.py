import random

throw1 = random.randrange(1, 7)
throw2 = random.randrange(1, 7)
throw3 = random.randrange(1, 7)

throw_sum = sum([throw1, throw2, throw3])
print(
    f'throw1: {throw1}, throw2: {throw2}, throw3: {throw3} \n sum: {throw_sum}')