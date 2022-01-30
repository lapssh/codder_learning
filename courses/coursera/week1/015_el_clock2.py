n = int(input())
hour = (n // 3600) % 24
min1 = ((n - (n // 3600) * 3600) // 60) // 10
min2 = ((n - (n // 3600) * 3600) // 60) % 10
sec1 = (n % 60) // 10
sec2 = (n % 60) % 10
print('{}:{}{}:{}{}'.format(hour, min1, min2, sec1, sec2))
