import math

height_cm = 170
cm_in_inches = 0.3937008
inches = height_cm * cm_in_inches

print(f'{math.ceil(inches // 12)} feet and {math.ceil(inches % 12)} inches')