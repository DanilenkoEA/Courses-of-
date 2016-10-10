# coding: utf-8
x = input()
y = input()
y = int(y)
x = int(x)


def division(m, n):
    if n > 0:
        rem = m - (m / n * n)
        return rem
    else:
        pass

print division(x, y)
