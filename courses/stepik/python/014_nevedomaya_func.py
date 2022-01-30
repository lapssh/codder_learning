# Напишите программу, на вход которой на первой строке подаётся число $n$, после этого на $n$ строках передаются
# числа $x_i$.
# Для каждого числа $x_i$ на отдельной строке выведите значение $f(x_i)$. Функция f(x) уже реализована и доступна для
# вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x. Для того, чтобы уложиться в
# ограничение по времени, нужно сохранять вычисленные значения.
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41
def f(x):
    return x * x


n = int(input())
memory = {}
for i in range(1, n + 1):
    x = int(input())
    if x in memory:
        print(memory[x])
    else:
        memory[x] = f(x)
        print(f(x))



    #print(f(x))

#for i in numbers:
#    print(i)

# 5   #ввод n - кол-во чисел
#
# 5   #ввод первое число х
#
# 11 #вывод значение функции f(5)
#
# 12    # ввод второго х
#
# 41     # вывод f(12)
#
# 9      #  ввод третьего x
#
# 47    # вывод f(9)
#
# 20     # ввод четвертого x
#
# 61     # вывод f(20)
#
# 12    # ввод пятого x
#
# 41    # вывод f(12)