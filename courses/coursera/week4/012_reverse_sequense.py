def reverse_s():
    n = input()
    if n != '0':
        reverse_s()
        print(n)
    else:
        print('0')


reverse_s()
