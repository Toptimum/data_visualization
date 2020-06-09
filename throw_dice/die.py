from random import randint


class Die:
    """ Класс кубика """

    def __init__(self, num_sides=6):
        """ По умолчанию используем шестигранный кубик """
        self.num_sides = num_sides

    def roll(self):
        """ Возвращаем случайное число от 1 до числа граней """
        return randint(1, self.num_sides)
