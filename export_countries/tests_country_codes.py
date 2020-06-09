from unittest import TestCase
from export_countries.country_codes import get_country_code


class TestCountryCodes(TestCase):
    """ Класс тестирования функции get_country_code из модуля country_codes """

    def test_return_correct_code(self):
        """ Тестируем корретное получение двузначного кода страны """
        code = get_country_code('Ukraine')
        self.assertEqual(code, 'ua')

    def test_return_code_for_exception_country(self):
        """ Тестируем корретное получение двузначного кода страны с исключительным названием """
        code = get_country_code('Russia')
        self.assertEqual(code, 'ru')

    def test_return_code_none(self):
        """ Тестируем получение значения None для не найденной материка/страны/города """
        code = get_country_code('Moskva')
        self.assertEqual(code, None)
