def IsPointInCircle(x, y, xc, yc, r):
    return (y - yc) ** 2 + (x - xc) ** 2 <= r ** 2


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
# (y-Yx)**2 + (x-Xc)**2 <= R**2
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
