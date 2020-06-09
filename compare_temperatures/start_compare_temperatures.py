from csv import reader
from matplotlib import pyplot
from datetime import datetime


def read_file(filename):
    """ Функция чтения файлов """
    file_obj = open(filename)
    data_file = reader(file_obj)
    return data_file


def extract_data(data_file_in):
    """ Извлекаем даты и температуру """
    dates_in, temperatures_in = [], []
    for row in data_file_in:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            fahrenheit_temperature = float(row[2])
            celsius_temperature = translate_fahrenheit_to_celsius(fahrenheit_temperature)
        except ValueError:
            print("Ошибка данных в файле, строчка пропущена.")
        else:
            dates_in.append(current_date)
            temperatures_in.append(celsius_temperature)
    return dates_in, temperatures_in


def translate_fahrenheit_to_celsius(temperature_fahrenheit):
    """ Функция перевода Фаренгейт в Цельсии с округлением """
    return int((temperature_fahrenheit - 32) / 1.8)


def add_plot(filename, name_city, color):
    """ Отображение линии на графике """
    data_file = read_file(filename)
    dates, temperatures = extract_data(data_file)
    pyplot.plot(dates, temperatures, c=color, alpha=0.5, label=name_city)


if __name__ == '__main__':
    filename_moscow = 'moscow.csv'
    filename_ottawa = 'ottawa.csv'
    filename_san_francisco = 'san-francisco.csv'

    # визуализация данных
    fig = pyplot.figure()
    pyplot.title(f"Часовой график температур\n(апрель-май 2020)", fontsize=20)
    pyplot.xlabel("Даты и время")
    fig.autofmt_xdate()
    pyplot.ylabel("Температура в °C")

    add_plot(filename_moscow, 'г. Москва (Россия)', 'red')
    add_plot(filename_ottawa, 'г. Оттава (Канада)', 'blue')
    add_plot(filename_san_francisco, 'г. Сан-Франциско (США)', 'orange')

    pyplot.legend()
    pyplot.show()
