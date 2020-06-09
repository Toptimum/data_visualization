from csv import reader
from pygal_maps_world import maps

from export_countries.country_codes import get_country_code


def read_file(name_file_in):
    """ Функция чтения файлов """
    file_object_in = open(name_file_in)
    data_file_in = reader(file_object_in)
    for _ in range(5):  # пропускаем первые 5 строк файла
        next(data_file_in)
    return data_file_in


def extract_data(data_file_in):
    """ Извлекаем название страны и процент экспорта за последний возможный год """
    countries_export_in = {}
    for row in data_file_in:
        try:
            for num in row[::-1]:  # ищем данные начиная с последних лет (инверсия)
                if num:
                    code = get_country_code(row[0])  # по названию страны получаем двузначный код Pygal
                    if code:
                        countries_export_in[code] = round(float(num), 1)
                        break
        except ValueError:
            print("Ошибка в данных.")
    return countries_export_in


def visual_map(countries_export_in):
    """ Визуализируем данные на карте """
    # визуализируем данные на карте мира
    world_map = maps.World()
    world_map.title = "Экспорт товаров и услуг (% от ВВП) за последние года"
    world_map.add("Страны", countries_export_in)
    world_map.render_to_file('export_countries.svg')
    print("Файл карты успешно создан - октройте в браузере.")


if __name__ == '__main__':
    file_name = 'API_NE.EXP.GNFS.ZS_DS2_en_csv_v2_1123320.csv'
    # считываем содержимое файла
    data_file = read_file(file_name)
    # получаем необходимые данные
    countries_export = extract_data(data_file)
    # визуализация данных
    visual_map(countries_export)
