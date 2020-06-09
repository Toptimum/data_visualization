from throw_dice.die import Die
from pygal import Bar

# создание кубиков
die_1 = Die(8)
die_2 = Die(8)

# моделирование серии бросков с сохранением данных
max_throws = 10000
results = [die_1.roll() + die_2.roll() for roll_num in range(max_throws)]
print(results)

# анализ результатов
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]
print(frequencies)

# визуализация результатов
histogram = Bar()
histogram.title = f"Результаты брасания двух кубиков {max_throws} раз"
histogram.x_labels = [num for num in range(2, max_result + 1)]
histogram.x_title = "Сумма выпадений"
histogram.y_title = "Количество выпадений"
histogram.add("Сумма граней кубиков", frequencies)
histogram.render_to_file('dice_visual.svg')
