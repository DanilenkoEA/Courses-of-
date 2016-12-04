# coding: utf-8
read = open("tutorial.txt")
write = open("write.txt", "w")
line = read.readlines()
for i in line:
    if "1" in i:
        continue
    if "2" in i:
        continue
    if "8" in i:
        break
    write.write(i)
write.close()
read.close()