cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]
person = 3  # int(input('Введите колличество персон:'))
# person = 5 #int(input('Введите колличество персон:')) # для указанного колличества

for recept in cook_book:
    print(f'{recept[0].capitalize()}:')  # построчно блюда и инкридиенты
    for incrediendts in recept[1]:
        new_netto = person * incrediendts[1]
        print(f'{incrediendts[0]}, {new_netto} {incrediendts[2]}')
    print()
