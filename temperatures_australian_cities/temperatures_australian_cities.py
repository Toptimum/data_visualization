from csv import reader
from matplotlib import pyplot
from collections import OrderedDict


def extract_data(data_file_in):
    """ Извлекаем города и значения температур (мин и макс) """
    temperatures_in_cities_in = {}
    for row in data_file_in:
        if row[1] not in temperatures_in_cities_in.keys():
            temperatures_in_cities_in[row[1]] = []
        if row[2] != 'NA' and row[3] != 'NA':
            temperatures_in_cities_in[row[1]].append(float(row[2]))
            temperatures_in_cities_in[row[1]].append(float(row[3]))
    return temperatures_in_cities_in


def find_min_max_temperatures(temperatures_in_cities_in):
    """ Из всех температур города, определяем мин и макс """
    for key_in, value_in in temperatures_in_cities_in.items():
        temperatures_in_cities_in[key_in] = [min(value_in), max(value_in)]
    return temperatures_in_cities_in


def add_bar(names_cities_in, temperature_in, opacity, color):
    """ Добавление столбца диаграммы на общий график """
    pyplot.bar(names_cities_in, temperature_in, alpha=opacity, color=color)
    #pyplot.annotate(str(temperature_in), xy=(names_cities_in, temperature_in), xytext=(names_cities_in, temperature_in))


def create_plot(min_max_temperatures_in_cities_in):
    """ Создаем график с барами """
    fig = pyplot.figure()
    pyplot.title(f"Диаграмма min и max температур\nпо городам Австралии (2008-2017 гг.)", fontsize=20)
    pyplot.xlabel("Города")
    pyplot.ylabel("Min и Max температура")
    # добавляем столбцы по значениям
    for key, value in min_max_temperatures_in_cities_in.items():
        add_bar(key, value[1], 0.5, 'orange')  # сначала рисуем столбец max температуры
        add_bar(key, value[0], 0.6, 'blue')  # затем сверху накладываем столбец холодной температры

    fig.autofmt_xdate()  # названия городов выводим по диагонали
    # разворачиваем окно на весь экран
    mng = pyplot.get_current_fig_manager()
    mng.window.state('zoomed')
    # выводим
    pyplot.show()


def read_file(filename_in):
    """ Функция чтения файла """
    file_obj = open(filename_in)
    data_file_in = reader(file_obj)
    next(data_file_in)  # пропускаем первую строку с заголовками
    return data_file_in


filename = 'weatherAUS.csv'

if __name__ == "__main__":
    # считываем содержимое файла
    data_file = read_file(filename)
    # извлекаем необходимые данные (города и осадки)
    temperatures_in_cities = extract_data(data_file)
    # вычисляем среднее значение осадков
    min_max_temperatures_in_cities = find_min_max_temperatures(temperatures_in_cities)
    min_max_temperatures_in_cities = OrderedDict(sorted(min_max_temperatures_in_cities.items(),
                                                        key=lambda t: t[0]))  # сортируем города по алфавиту
    # строим график
    create_plot(min_max_temperatures_in_cities)
