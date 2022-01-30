def MinDivision(n):
    norm_div = int(n ** 0.5)
    for i in range(2, norm_div + 1):
        if (n / i).is_integer():
            return i
    return int(n)


n = int(input())
print(MinDivision(n))
