def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                [arr[j-1], arr[j]] = [arr[j], arr[j-1]]
    return arr


print(bubble_sort([43, 41, 5, 52, 157, -2, 242, 53]))
print(bubble_sort([-4, -39, 5, -5, 34, 545, 26, 6]))
print(bubble_sort([0, 2, -1, -2, 50, -4, 10, -3]))
