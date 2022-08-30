array = input().split(" ")

pointA_x = 0
pointA_y = 0

x_min = 0
y_min = 0
if int(array[0]) <= int(array[2]) - int(array[0]):
    x_min = int(array[0])
else:
    x_min = int(array[2]) - int(array[0])

if int(array[1]) <= int(array[3]) - int(array[1]):
    y_min = int(array[1])
else:
    y_min = int(array[3]) - int(array[1])

if x_min < y_min:
    print(x_min)
else:
    print(y_min)