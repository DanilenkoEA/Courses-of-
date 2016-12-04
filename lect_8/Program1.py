# coding: utf-8
x = 0

while x < 10:
    x += 1
    file = open("tutorial.txt", "a")
    file.write(str(x))
    file.write("\r\n")
    file.close()
