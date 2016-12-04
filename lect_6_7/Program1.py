# coding: utf-8

y = raw_input("Enter value\t\n")
x = ''.join(y.split())

if "+" in x:
    first = x[:x.find("+")]
    second = x[x.find("+")+1:]
    print float(first) + float(second)
elif "-" in x:
    first = x[:x.find("-")]
    second = x[x.find("-")+1:]
    print float(first) - float(second)
elif "*" in x:
    first = x[:x.find("*")]
    second = x[x.find("*")+1:]
    print float(first) * float(second)
elif "/" in x:
    first = x[:x.find("/")]
    second = x[x.find("/")+1:]
    print float(first) / float(second)
elif "%" in x:
    first = x[:x.find("%")]
    second = x[x.find("%")+1:]
    print float(first) % float(second)
