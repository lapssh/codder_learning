# ax**2 + bx + c = 0
# discriminant D = b**2 - 4ac
# test 1
# a = 1.0
# b = -1.0
# c = -2.0
# test 2
# a = 1.0
# b = 2.0
# c = 1.0
# test  3
# a = 1.0
# b = -7.5
# c = 3.0
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c
# print(d)
if d == 0:
    x = -b / (2 * a)
    print(x)
elif d > 0:
    x1 = round((-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), 6)
    x2 = round((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), 6)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif d < 0:
    pass
