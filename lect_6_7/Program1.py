# coding: utf-8

x = raw_input("Enter value\n")

if "+" in x:
    first = x[:x.index("+")]
    second = x[x.index("+")+1:]
    print float(first) + float(second)
elif "-" in x:
    first = x[:x.index("-")]
    second = x[x.index("-")+1:]
    print float(first) - float(second)
elif "*" in x:
    first = x[:x.index("*")]
    second = x[x.index("*")+1:]
    print float(first) * float(second)
elif "/" in x:
    first = x[:x.index("/")]
    second = x[x.index("/")+1:]
    print float(first) / float(second)
elif "%" in x:
    first = x[:x.index("%")]
    second = x[x.index("%")+1:]
    print int(first) % float(second)