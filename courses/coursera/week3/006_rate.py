# rate = 12
# rubl = 179
# koop = 0
rate = int(input())
rubl = int(input())
koop = int(input())

deposit = rubl + koop / 100
percent = deposit * rate / 100
percent = percent * 100
percent = int(percent)
percent = percent / 100

# print(percent)
profit = deposit + percent
print(int(profit), round((profit - int(profit)) * 100))
