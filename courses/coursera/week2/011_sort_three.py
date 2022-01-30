a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    (a, c) = (c, a)
    if a > b:
        (b, a) = (a, b)
elif b >= a and b >= c:
    (c, b) = (b, c)
    if a > b:
        (b, a) = (a, b)
elif a > b:
    (b, a) = (a, b)

print(a, b, c)
