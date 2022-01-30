# По данному числу n вычислите сумму
# (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += 1 / i ** 2
print(round(sum, 6))
