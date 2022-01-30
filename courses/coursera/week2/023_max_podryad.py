n = 1
my_list = []
while n != 0:
    n = int(input())
    my_list.append(n)
count = 0
eqvil = my_list[0]
max_count = 0

for i in range(1, len(my_list)):
    if my_list[i] == eqvil:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
        eqvil = my_list[i]
# if max_count != 0:
print(max_count + 1)
# else:
#     print(max_count)
