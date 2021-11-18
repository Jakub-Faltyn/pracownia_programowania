import random

def rand_elem(arr):
    idx = random.randint(0, len(arr) - 1)
    return arr[idx]

print(
    rand_elem([1, 2, 3, 4, 5, 6])
)
