import math

n = input()
l = len(n) - 1
index = 0
for i in range (pow(10, l), int(n)):
    array = map(int, list(str(i)))
    temp = sum(array) + i
    if temp == int(n):
        print(i)
        break
    index = index + 1
else:
    print(0) 