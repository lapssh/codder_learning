# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
# следующая информация:
#
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#
# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю
# оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
#
# Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому
# языку по всем абитуриентам.
#
# В качестве ответа на задание прикрепите полученный файл со средними оценками.
#
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']

def file_to_list(filename):
    marks = []
    num = 0
    with open(filename, 'r') as inf:
        for line in inf:
            s = line.strip().split(';')
            marks.append(s)
            num += 1
    return marks


def calculate(list_marks):
    avg_matan = 0
    avg_phithics = 0
    avg_russian = 0
    number_of_students = 0
    with open('answer.txt', 'w') as ouf:
        for i in list_marks:
            avg = ((int(i[1]) + int(i[2]) + int(i[3])) / 3)
            number_of_students += 1
            avg_matan += int(i[1])
            avg_phithics += int(i[2])
            avg_russian += int(i[3])
            print(round(avg, 9))
            print(number_of_students, i)
            ouf.write(str(round(avg, 9)) + '\n')
    avg_all_matan = round((avg_matan / number_of_students), 9)
    avg_all_phithics = round((avg_phithics / number_of_students), 9)
    avg_all_russian = round((avg_russian / number_of_students) ,9)
    itogo = str(avg_all_matan) + ' ' + str(avg_all_phithics) + ' ' + str(avg_all_russian)
    print(itogo)
    print('blyat')
    with open('answer.txt', 'a') as ouf:
        ouf.write(itogo)



# def list_to_file(list_final):
#     with open('answer.txt', 'w') as ouf:
#         ouf.write(list_final)


# Begin
res = file_to_list('students_marks.txt')
to_output = calculate(res)
# list_to_file(to_output)

