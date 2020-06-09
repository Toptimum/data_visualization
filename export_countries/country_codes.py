from pygal_maps_world import i18n


def get_country_code(country_name_in):
    """ Для страны возвращаем ее код из Pygal """
    countries_exception = {'Vietnam': 'vn', 'Bolivia': 'bo', 'Yemen, Rep.': 'ye', 'Venezuela, RB': 've',
                           'Moldova': 'md', 'Egypt, Arab Rep.': 'eg', 'Libya': 'ly', 'Tanzania': 'tz',
                           'Iran, Islamic Rep.': 'ir', 'Congo, Dem. Rep.': 'cd', 'Congo, Rep.': 'cg',
                           'Kyrgyz Republic': 'kg', 'Russia': 'ru', 'DR Congo': 'cd', 'Iran': 'ir'}
    for code in i18n.COUNTRIES.keys():
        if i18n.COUNTRIES[code] == country_name_in:  # сначала ищем строгое соответствие
            return code
        elif country_name_in in countries_exception:  # затем ищем соответствие в странах исключениях
            return countries_exception[country_name_in]
    return None  # возвращаем None, если ничего не нашли
