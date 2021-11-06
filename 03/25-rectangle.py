
height = int(input("Enter a side: "))
width = int(input("Enter b side: "))

print()

for i in range(height):
    if (i == 0) or (i == height - 1):
        print(width * "*")
    else:
        print("*" + " " * (width - 2) + "*")

print()