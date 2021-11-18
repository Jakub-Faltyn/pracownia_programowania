def unique_elements(arr):
    unique = []
    for el in arr:
        if not el in unique:
            unique.append(el)
    return unique


print(unique_elements([1, 20, 3, 20, 30, 2, 1, 3]))
