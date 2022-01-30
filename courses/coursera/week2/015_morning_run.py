x = int(input())
y = int(input())
a = x / 100 * 10
day = 1
if x == y:
    day = 0
dist = x
while dist <= y:
    dist += a
    day += 1
    if dist >= y:
        break
    x = x + a
    a = x / 100 * 10
print(day)
