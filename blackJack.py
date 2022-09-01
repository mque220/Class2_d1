n_m = input().split(" ")

n = int(n_m[0])
maximum = int(n_m[1])
get_sum = 0
nums = input().split(" ")

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            temp = int(nums[i]) + int(nums[j]) + int(nums[k])
            if get_sum <= temp and temp <= maximum:
                get_sum = temp
            if get_sum == maximum:
                break
print(get_sum)