a = int(input())
b = int(input())
c = int(input())
d = int(input())  # окно
e = int(input())  # окно

if a <= d and b <= e:
    print('YES')
elif b <= d and a <= e:
    print('YES')
elif b <= d and c <= e:
    print('YES')
elif c <= d and b <= e:
    print('YES')
elif a <= d and c <= e:
    print('YES')
elif c <= d and a <= e:
    print('YES')
elif a <= e and b <= d:
    print('YES')
elif b <= e and a <= d:
    print('YES')
elif b <= e and c <= d:
    print('YES')
elif c <= e and b <= d:
    print('YES')
elif a <= e and c <= d:
    print('YES')
elif c <= e and a <= d:
    print('YES')
else:
    print('NO')
