# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”,
# “n коровы”, правильно склоняя слово “корова”.
#
# Формат ввода
#
# Вводится натуральное число.
#
# Формат вывода
#
# Программа должна вывести введенное число n и одно из слов: korov,
# korova или korovy. Между числом и словом должен стоять ровно один пробел.

# "n коров", если 10 < n < 20 или последняя цифра
#  n - одна из 0, 5, 6, 7, 8, 9.
# "n корова", если последняя цифра n == 1.
# "n коровы" во всех остальных случаях.

n = input()
numbers = ['0', '5', '6', '7', '8', '9']
if 10 < int(n) < 20:
    print(n, 'korov')
elif str(n[-1]) in numbers:
    print(n, 'korov')
elif str(n[-1]) == '1':
    print(n, 'korova')
else:
    print(n, 'korovy')
