def even_and_odd(arr):
    arr.sort(key=is_even)
    return arr

def is_even(num):
    return num % 2 == 1

print(even_and_odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
