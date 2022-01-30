# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.

#def modify_list(l):
#	l2 = []
#	for i in range (0,len(l)):
#		if int(l[i]) % 2 == 0:
#			l2.append(int(l[i]/2))
#	return l2
def modify_list(l):
	for i in range(0,len(l)):
		print ('i=',i,' а l[i]=',l[i])
		if int(l[i]) % 2 == 0:
			l[i] = int(l[i]/2)
		elif int(l[i] % 2 != 0):
			l[i] = 666

	while 666 in l:
		l.remove(666)
	return l


l = [int(i) for i in input().split()]
print(modify_list(l))
