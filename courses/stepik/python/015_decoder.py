def code_line(s):
    cod = ''
    num = 1
    i = 0
    while i !=len(s):
        char = s[i]
        i += 1
        if i == len(s):
            break
        if s[i] == char:
            num =  num + 1
        else:
            cod = cod + char + str(num)
            char = s[i]
            num = 1
    cod = cod + char + str(num)
    return cod


def decode_line(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    decode = ''
    i = 0
    while i !=  len(s):
        char = s[i]
        i += 1
        if i == len(s):
            break
        while s[i] in numbers:
            num = s[i]
            if i+1 < len(s) and s[i+1] in numbers:
                num = s[i]+s[i+1]
                i += 1
            break
        if char not in numbers:
            decode = decode + (char * int(num))
    return decode

with open('dataset_3363_2.txt', 'r') as inf:
    s = inf.readline().strip()
    my_decode = decode_line(s)
    my_code = code_line(my_decode)
    answer = decode_line(s)
    print('Строка из файла:', s)
    print('Моя расшифровка: ', my_decode)
    print('Моё кодирование: ',my_code)
    if my_code == s:
        print('you Красавчег!')




