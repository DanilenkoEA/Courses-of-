# coding: utf-8

array = [1, 0, 9, 5, 3, 8, 4, 6, 2]
n = len(array)
m = n - 1
while m > 0:
    for i in range(m):
        if (array[i] > array[i + 1]):
            x = array[i]
            array[i] = array[i + 1]
            array[i + 1] = x
    m = m - 1

print array

assert array == sorted(array)
