def my_pow(a, n, result=1):
    while n != 0:
        result *= a
        n -= 1
        my_pow(a, n, result)
    return result


a = float(input())
n = int(input())
# n = n
if a == 0:
    print('0')
else:
    print(my_pow(a, n))
