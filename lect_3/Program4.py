# coding: utf-8
y = 63.5


def convert(x):
    fx = x / y
    return fx

print ('Vvedite summu v rub:')
x = convert(round(input(), 2))
print 'Summa v valute:', x
