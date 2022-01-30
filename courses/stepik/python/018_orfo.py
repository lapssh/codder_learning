# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество d d известных нам слов, после чего на  d d строках
# указываются эти слова. Затем передаётся количество  l l строк текста для проверки, после чего  l l строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# Sample Input:
#
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
# Sample Output:
#
# stepic
# champignons
# the
# Оптимальное решение:
# dic = {input().lower() for i in range(int(input()))}
#
# wrd = set()
# for w in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
# 
# print(*wrd.difference(dic), sep="\n")


def create_orfo_dict(num_words):
    orfo_dict = []
    for i in range(0, num_words):
        orfo_dict.append(input())
    return orfo_dict


# num_word = 4  # int(input())
# orfo_dict = ['champions', 'we', 'are', 'Stepik']
# num_lines = 3  # int(input())
# text = ['We are the champignons', 'We Are The Champions', 'Stepic']

def input_text(num_lines):
    text = []
    for i in range(0, num_lines):
        text.append(input())
    return text


def orfo_check(orfo_dict, text):
    errors_count = 0
    orfo = []
    for i in orfo_dict:
        orfo.append(i.lower())
    set_errors = set()
    for i in text:
        line = i.split()
        for words in line:
            low_word = words.lower()
            if low_word not in orfo:
                set_errors.add(low_word)
    return set_errors


orfo_dict = create_orfo_dict(int(input()))
text = input_text(int(input()))

errors = orfo_check(orfo_dict, text)
for i in errors:
    print(i.lower())
