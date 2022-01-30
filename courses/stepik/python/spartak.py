# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n n — количество завершенных игр.
# После этого идет n n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
# Sample Output:
#
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1


def input_data():
    number_of_mathes = int(input())
    matches = []
    # Генерация списков матчей
    for i in range(0, number_of_mathes):
        match = input().split(';')
        matches.append(match)
    return matches


def create_list_of_clubs(data):
    '''
    Строим словарь, где ключ - имя команды, а [0,0,0,0,0] - матчи(0), победы(1), ничьи(2), поражения(3), счет (4)
    :param data:
    :return:
    '''
    club_list = {}
    for i in range(0, len(data)):
        for j in range(0, 4):
            if j == 0:
                if data[i][j] not in club_list:
                    club_list[data[i][j]] = [0, 0, 0, 0, 0]
            if j == 2:
                if data[i][j] not in club_list:
                    club_list[data[i][j]] = [0, 0, 0, 0, 0]
#    print(club_list)
    return club_list


def create_tournir(clubs, data):
    '''
    Функиця подсчета очков
    :param data: - вложенный список с результатами
    :return:
    '''
    for i in range(0, len(data)):
        score1 = clubs[data[i][0]]
        score2 = clubs[data[i][2]]
        # подсказка [0]-матчи [1]-победы  [2]-ничьи [3]-поражения [4]-счет
        name1 = data[i][0]
        name2 = data[i][2]
        if data[i][1] > data[i][3]:
            score1[0] += 1
            score1[1] += 1
            score1[4] += 3
            score2[0] += 1
            score2[3] += 1
        elif data[i][1] < data[i][3]:
            score1[0] += 1
            score1[3] += 1
            score2[0] += 1
            score2[1] += 1
            score2[4] += 3
        elif data[i][1] == data[i][3]:
            score1[0] += 1
            score1[2] += 1
            score1[4] += 1
            score2[0] += 1
            score2[2] += 1
            score2[4] += 1
        clubs[name1] = score1
        clubs[name2] = score2
    return clubs


def display_result(res):
    for x in res:
        print(x, ':', str(res[x]).replace(',', '').replace('[', '').replace(']', ''), sep='')


# matches = input_data()
matches = [['Зенит',3,'Спартак',1],['Спартак',1,'ЦСКА',1],['ЦСКА',0,'Зенит',2]]
# matches = [['Франция', 1, 'Румыния', 1],['Албания', 0, 'Швейцария', 1],['Уэльс', 2, 'Словакия', 1]]


clubs = create_list_of_clubs(matches)  # вызываем построение турнирной таблицы
result = create_tournir(clubs, matches)
display_result(result)
