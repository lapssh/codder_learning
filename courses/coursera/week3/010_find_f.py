f = input()
if 'f' not in f:
    pass
else:
    first_index = f.find('f')
    f_revers = f[::-1]
    last_index = len(f) - f_revers.find('f') - 1
    if first_index != last_index:
        print(first_index, last_index)
    else:
        print(first_index)
