import math

a = float(input('Enter length of a side: '))
b = float(input('Enter length of b side: '))
c = float(input('Enter length of c side: '))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"traingle area: {area}")