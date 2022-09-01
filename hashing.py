M = 1234567891
r = 31
H = 0
m = 1

L = int(input())
arr = list(map(ord, list(input())))

for i in range(L):
    H = (H + ((arr[i] - 96) * m % M)) % M
    m = (m * r) % M

print(H)
