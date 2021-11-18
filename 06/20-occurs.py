def occurs(num, arr):
    return num in arr

num = 5
if occurs(num, [1, 3, 4, 2, 6, 5]):
    print(f"Number {num} appears in the array")
else:
    print(f"Number {num} does not appear in the array")
