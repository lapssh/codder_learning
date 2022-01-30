a = int(input())
b = int(input())
n = int(input())

total_cost = a * 100 + b
print((n * total_cost) // 100, (n * total_cost) % 100)
