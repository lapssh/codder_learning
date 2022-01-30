# s = 'coffee'
s = input()
if 'f' not in s:
    print('-2')
else:
    pos1 = s.find('f')
    s2 = s[pos1 + 1:]
    if 'f' not in s2:
        print('-1')
    else:
        print(s2.find('f') + pos1 + 1)
