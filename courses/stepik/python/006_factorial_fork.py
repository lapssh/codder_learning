# Напишите программу, которая выводит часть последовательности
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
a = []
n = int(input())
for i in range(0,n+1):
	for j in range(0,i):
		a.append(i)
#print (a)

for i in range(0,n):
	print (a[i], ' ', end = '')
