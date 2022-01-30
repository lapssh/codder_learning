x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

pos1 = x1 - x2
pos2 = y1 - y2

if pos1 <= 1:
    if pos1 >= -1:
        if pos2 <= 1:
            if pos2 >= -1:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
