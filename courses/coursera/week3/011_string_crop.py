# s = 'In the hole in the ground there lived a hobbit'
s = input()
pos1 = s.find('h')
s_mirror = s[::-1]
pos2 = len(s) - s_mirror.find('h')
result = s[:pos1] + s[pos2:]
print(result)
