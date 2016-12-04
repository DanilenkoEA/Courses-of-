# coding: utf-8
x = 0

while x < 10:
    x += 1
    f = open("tutorial.txt", "a")
    f.write(str(x))
    f.write("\r\n")
    f.close()
