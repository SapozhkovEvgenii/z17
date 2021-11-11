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

sum_min = sum(arr[0])
for i in range(n):
    if sum(arr[i]) < sum_min:
        sum_min = sum(arr[i])

for index_row_min in range(n):
    if sum(arr[index_row_min]) == sum_min:
        print(index_row_min)




