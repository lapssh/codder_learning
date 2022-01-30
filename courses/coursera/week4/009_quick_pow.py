def quick_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n - 1) * a
    else:
        return pow(a ** 2, n // 2)


a = float(input())
n = int(input())
print(quick_pow(a, n))
