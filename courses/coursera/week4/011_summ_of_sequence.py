def summa():
    n = int(input())
    if n != 0:
        return n + summa()
    return 0


print(summa())
