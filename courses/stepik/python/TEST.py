countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6, 55.4, 57.2]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4, 51.8]],
]
num = 0
item = 0
srednee = 0
for country in countries_temperature:
    print(country)
    for temp in country[1]:
        print(temp)
    # for i in range(1,len(country)):
    #     print(counti)
    #     item = item + i
    #     num += 1


 #   print(f'{country} средняя температура {5 / 9 * (sum - 32)}')