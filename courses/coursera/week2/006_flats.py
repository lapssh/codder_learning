# flat1 = int(input())
# flat2 = int(input())

flat1 = int(input())
flat2 = int(input())

number_of_flats = flat2 - flat1 + 1  # 5
if flat1 == 1:
    print('YES')
elif (flat1 - 1) % number_of_flats == 0:
    print('YES')
else:
    print('NO')
