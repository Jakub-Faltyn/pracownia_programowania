x = float(input('Enter value of x: '))
y = float(input('Enter value of y: '))

if x > 0:
    if y > 0:
        print(
            f"Point P({x},{y}) is in the first quadrant of the coordinate system")
    elif y < 0:
        print(
            f"Point P({x},{y}) is in the fourt quadrant of the coordinate system")
elif x < 0:
    if y < 0:
        print(
            f"Point P({x},{y}) is in the third quadrant of the coordinate system")
    elif y > 0:
        print(
            f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x == 0 and y == 0:
    print(
        f"Point P({x},{y}) is in the middle of the coordinate system")