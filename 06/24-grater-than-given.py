def grater_than_given(nums):
    given = int(input("Enter a number: "))
    grater = []
    for num in nums:
        if num > given:
            grater.append(num)
    return grater

res = grater_than_given([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(res)
