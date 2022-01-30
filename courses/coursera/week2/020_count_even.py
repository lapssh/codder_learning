count_even = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        count_even += 1
print(count_even)
