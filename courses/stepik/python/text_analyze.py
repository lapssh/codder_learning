# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
#
# В качестве ответа укажите вывод программы, а не саму программу.
#
# Слова, написанные в разных регистрах, считаются одинаковыми.
#
# Sample Input:
#
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
#
# abc 3
def analyze(text):
    words = text.lower().split()
    words2 = list(words)
    words2.sort()
    stat = {}
    for i in words2:
        if i in stat:
            stat[i] = stat[i] + 1
        else:
            stat[i] = 1
    return stat

def max_value(s):
    max_key = s.

s = 'abc a bCd bC AbC BC BCD bcd ABC'
print(analyze(s))
