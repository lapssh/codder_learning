# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests
def get_next(url):
    basic_url = 'https://stepic.org/media/attachments/course67/3.6.3/'
    r = requests.get(url)
    my_text = r.text
    print(my_text)
    if my_text[0:2] == 'We':
        return my_text
    get_next(basic_url + my_text)




with open('list_files.txt', 'r') as inf:
    my_url = inf.read().strip()
print(my_url)
answer = get_next(my_url)
print(answer)
