# Группа биологов в институте биоинформатики завела себе черепашку.
#
# После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
# север 10
# запад 20
# юг 30
# восток 40
# где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное
# расстояние в сантиметрах, которое должна пройти черепашка.
#
# Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая
# определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая
# выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается
# в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.
#
# Программе подаётся на вход число команд n n, которые нужно выполнить черепашке, после чего n n строк с самими
# командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки.
# Все координаты целочисленные.
#
# Sample Input:
#
# 4
# север 10
# запад 20
# юг 30
# восток 40
# Sample Output:
#
# 20 -20

# +x восток    -х запад    +у север    -у юг

#sample_input = ['север 10', 'запад 20', 'юг 30', 'восток 40']


def calculate_turtle(data):
    x = 0
    y = 0
    for line in data:
        kurs, val = line.split()
        if kurs == 'север':
            y +=  int(val)
        elif kurs == 'запад':
            x -= int(val)
        elif kurs == 'восток':
            x += int(val)
        elif kurs == 'юг':
            y -= int(val)
        else:
            print('ошибка ввода')
    return x,y

#n = int(input())

sample_input = []
n = int(input())
for i in range (n):
    sample_input.append(input())

x, y = calculate_turtle(sample_input)
print(x,y)