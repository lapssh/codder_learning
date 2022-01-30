def f(x):
	if x <= -2:
		res = (1-(x+2)*(x+2))
		return res
	elif x>2:
		res = (x-2)**2+1
		return res
	else:
		res = -(x/2)
		return res

print(f(2))