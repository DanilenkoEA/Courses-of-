# coding: utf-8
x = 0
y = 0
z = ""
znachenie = False

while znachenie == False:
    x = int(input("Введите значение X(от 1 до 3) \t"))
    y = int(input("Введите значение Y (от 1 до 3) \t"))
    z = raw_input("Крестик или Нолик? :) (X или О)\t").upper()

    if x < 1 or x > 3:
        print ("Значения X должно быть от 1 до 3")
    elif y < 1 or y > 3:
        print ("Значения Y должно быть от 1 до 3")
    elif z != "0" and z != "O" and z != "X":
        print ("Значение знака введено неверно")
    else:
        print "%s,%s:%s" % (x, y, z)
        znachenie = True
