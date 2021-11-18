def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                [arr[j-1], arr[j]] = [arr[j], arr[j-1]]
    return arr

def median(arr):
    sorted_arr = bubble_sort(arr)
    idx = len(arr) // 2
    if len(arr) % 2 == 0:
        return (arr[idx - 1] + arr[idx]) / 2
    else:
        return arr[idx]

print(median([1, 0, 9, 4, 6]))
print(median([6, 8, 3, 1, 0, 5, 7]))
