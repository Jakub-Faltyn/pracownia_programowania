first = [4, 36, 12, 28, 9, 44, 5]
second = [5, 1, 36]

def unique_numbers(a, b):
    unique = []
    for num in a:
        if not num in b:
            unique.append(num)
    return unique

print(unique_numbers(first, second))
