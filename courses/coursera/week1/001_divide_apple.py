# N школьников поделили K яблок поровну, не делящийся
# остаток остался в корзинке. Сколько яблок осталось в корзинке?
#
# Формат ввода
#
# Программа получает на вход числа N и K — натуральные, не превышают 10000.
#
# Формат вывода
#
# Выведите ответ на задачу.

n = int(input())  # колличество школоты
k = int(input())  # колличество яблок

print(k % n)