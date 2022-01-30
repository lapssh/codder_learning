max1 = ''
while True:
    n = int(input())
    if n == 0:
        break
    max2 = n
    if max1 == '':
        max1 = max2
    if max2 > max1:
        max1, max2 = max2, max1

print(max2)
