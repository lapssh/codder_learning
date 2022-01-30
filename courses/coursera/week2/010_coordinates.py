x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 > 0 and x2 > 0:
    if y1 > 0 and y2 > 0:
        print('YES')  # 1
    elif y1 < 0 and y2 < 0:
        print('YES')  # 2
    else:
        print('NO')
elif x1 < 0 and x2 < 0:
    if y1 > 0 and y2 > 0:
        print('YES')  # 3
    elif y1 < 0 and y2 < 0:
        print('YES')  # 4
    else:
        print('NO')
else:
    print('NO')
