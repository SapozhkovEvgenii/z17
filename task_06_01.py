from random import randint

n = 3
m = 4
arr = []

for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(1, 9)
        arr1.append(p)
    arr.append(arr1)

print(arr)