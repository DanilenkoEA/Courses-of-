# coding: utf-8

i = 1


def func(x):
    y = 2
    while y <= x / 2:
        if x % y != 0:
            return True
        y += 1


while i != 0:
    i = input('Введите число: \n')
    if func(i) == True:
        print "Простое число"
    else:
        print "Композитное число"
