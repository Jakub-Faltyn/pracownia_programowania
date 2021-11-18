def sum_of_digits(num):
    sum = 0
    string = str(num)
    for i in string:
        sum += int(i)
    return sum


print(sum_of_digits('7182'))
