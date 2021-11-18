colors = ["red", "green", "pink", "blue", "white"]


file = open('colors.txt', 'a')
for color in colors:
    file.write(color + "\n")
file.close()
