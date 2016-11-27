# coding: utf-8

# Первый вариант (не получается для чисел) :(
x = ['a', 'b', 'c']


def reverse(y):
    z = []
    for i in xrange(len(y)-1, -1, -1):
        z += y[i]
    return z
print reverse(x)

# assert reverse(x) == list(reversed(x))

# # Второй вариант

# x = [0, 10, 20, 40]
# y = x[::-1]
# print y
# assert y == list(reversed(x))
