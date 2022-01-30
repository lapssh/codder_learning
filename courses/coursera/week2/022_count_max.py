n = 1
my_list = []
while n != 0:
    n = int(input())
    my_list.append(n)
my_list.sort()
count = 0
max = my_list[-1]
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == max:
        count += 1

print(count)
