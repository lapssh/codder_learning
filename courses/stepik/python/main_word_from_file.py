# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
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

def calculate__max_word(s):
    dict_words = {}
    for word in s:
        if word not in dict_words:
            #print(word, 'нет с словаре')
            dict_words[word] = 1
            #print(dict_words)
        else:
            dict_words[word] += 1
    # теперь нужно вытащить только самые повторяющиеся слова
    max_num = dict_words.values()
    max_num = max(max_num)
    set_max_words = set()
    for key in dict_words:
        if dict_words[key] == max_num:
            set_max_words.add(key)

    #print (max_num)
    #print(set_max_words)
    print(min(set_max_words), max_num)



with open('input_data.txt', 'r') as inf:
    list_words = inf.read().lower().split()

max_words = calculate__max_word(list_words)
