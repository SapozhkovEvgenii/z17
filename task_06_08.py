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
my_list_index = []

for i in range(m):
    summa_elem = 0
    for j in range(n):
        summa_elem += arr[j][i]
    my_list_index.append(summa_elem)
print(my_list_index)
index_min_column = my_list_index.index(min(my_list_index))
print(index_min_column)




