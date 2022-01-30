import sys

parametrs = list()
for param in sys.argv:
    #print(param)
    parametrs.append(param)
parametrs = parametrs[1:]
for i in parametrs:
    print(i, ' ', end = '')