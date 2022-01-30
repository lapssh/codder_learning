# x=(de-fb)/(da-bc)
# y=(fa-ec)/(da-bc)
# test 3
# a = 3
# b = 5
# c = 4
# d = 4
# e = 11
# f = 12
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = (d * e - f * b) / (d * a - b * c)
y = (f * a - e * c) / (d * a - b * c)
print(x, y)
