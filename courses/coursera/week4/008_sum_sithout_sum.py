def sum(a, b):
    if b == 0:
        return a
    a = a + 1
    b = b - 1
    return sum(a, b)


a = int(input())
b = int(input())
print(sum(a, b))
