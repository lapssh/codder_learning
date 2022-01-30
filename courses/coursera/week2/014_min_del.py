n = int(input())
if n == 2:
    print('2')
elif n == 3:
    print('3')
else:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            break
