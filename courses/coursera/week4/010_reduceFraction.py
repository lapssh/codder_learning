def noc(a, b):
    if b == 0:
        return a
    else:
        return noc(b, a % b)


n = int(input())
m = int(input())
noc = noc(n, m)
print(int(n / noc), int(m / noc))
