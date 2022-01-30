def kvadrat(n):
    if n == 1:
        print(1)
    for i in range(1, n):
        kvadrat = i ** 2
        if kvadrat <= n:
            print(str(kvadrat) + ' ', end='')
        else:
            break


n = int(input())
kvadrat(n)
