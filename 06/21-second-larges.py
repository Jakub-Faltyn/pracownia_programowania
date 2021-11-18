def second_largest(arr):
    largest = arr[0]
    second = arr[0]
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num>second:
            second=num
    return second

print(
    second_largest([5, 1, 9, 6, 1])
)
