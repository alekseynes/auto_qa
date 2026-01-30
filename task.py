mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']

colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']

rainbow_colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']

rainbow_dict = {}
for i in range(len(mnemo)):
    rainbow_dict[mnemo[i]] = rainbow_colors[i]

print(rainbow_dict)