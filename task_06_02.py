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

max_element = arr[0][0]
for i in arr:
    for j in i:
        if j > max_element:
            max_element = j

print(max_element)
