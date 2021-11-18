def is_subset(a, b):
    for num in a:
        if not num in b:
            return False
    return True

print(is_subset([1, 2, 3], [1, 2, 3, 4, 5, 6]))
