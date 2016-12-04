# coding: utf-8
f = open("tutorial.txt")
r = open("write.txt", "w")
file = f.readlines()
for i in file:
    if "1" in i:
        continue
    if "2" in i:
        continue
    if "8" in i:
        break
    r.write(i)
r.close()
f.close()
