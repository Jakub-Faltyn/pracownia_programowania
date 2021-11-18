def join(arr):
    res = ""
    for i in range(len(arr)):
        if i == len(arr) - 1:
            res += str(arr[i])
        else:
            res += str(arr[i]) + ","
    return res

def join(arr): return ",".join([str(num) for num in arr])

print(
    join([5, 4, 3, 2, 6, 5])
)
print(
    join([5, 4, 3, 2, 6, 5])
)
