def IsPrime(n):
    max_div = int(n ** 0.5)
    for divisor in range(2, max_div + 1):
        if n % divisor == 0:
            return 'NO'
    return 'YES'


n = int(input())
print(IsPrime(n))
