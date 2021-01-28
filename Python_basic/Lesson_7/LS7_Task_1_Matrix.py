""" Author: Maksim Sapunov msdir6199@gmail.com 26/01/2021"""

# Задача 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.


from random import randint
from typing import List

# Примечание: Согласно условию задачи принято реализовать решение не используя Pandas :).

# 1. Создание вспомогательной функции для формирования псевдорандомных списков.


def random_list(length):  # Создаем псевдорандомный список (частный случай для целых чисел от 0 до 99)
    """
    Функция создает список длиной length из псевдослучайных целых чисел от 0 до 99
    :param length - int длина списка
    :return random_list
    """
    return [randint(0, 99) for el in range(length)]  # !Синяя изолента! PyCharm 'ругается' на el


# 2. Объявление класса для создания и управления матрицами
class Matrix:
    """ Класс содержит методы создания и управления матрицами"""
    mtr: List[List[int]]
    _number_of_created_matrix = 0

    def __init__(self, length):
        """ Функция инициирует конструктор класса"""
        self.length = length
        self.mtr = [random_list(self.length) for el in range(self.length)]  # !Синяя изолента! PyCharm 'ругается' на el
        # создается матрица псевдорандомных чисел используя ранее созданную функцию random_list
        Matrix._number_of_created_matrix += 1  # Увеличиваем счетчик матриц для удобства дальнейшей обработки

    def __str__(self):
        """ Функция реализует перегрузку оператора str """
        for links in self.mtr:
            for element in links:
                separator = ('--' if int(links.index(element)) < len(links)-1 else '')
                #  !Синяя изолента! Работает, но изредка (?) выдает '--' по завершении вывода строки на экран.
                print(self.get_format_output(element), end=separator)
            print('')
        return '~~~~~'*self.length
        # При запросе вывода матрицы на экран выводится представление матрицы и завершающий декор.

    def __add__(self, other):
        """ Функция обеспечивает перегрузку оператора сложения"""
        mtr_3 = Matrix(self.length)
        mtr_3.mtr = [[(self.mtr[link][el] + other.mtr[link][el]) for el in range(self.length)]
                     for link in range(self.length)]
        # Cуммирование данных матриц 1 и 2 было осуществлено двумя вложенными генераторами списка
        return mtr_3

    def get_int_descriptive_output(self):
        """ Функция обеспечивает аккуратный 'читабельный' вывод матрицы на экран используя числовое представление"""
        # Первое решение, при анализе кода выяснилось что не соответствует условию задачи
        # Выполнено решение через реализацию перегрузки __str__
        decor = '*****' * self.length
        print(f'Представление матрицы # {Matrix._number_of_created_matrix}', decor, sep='\n')
        for el in self.mtr:
            for i in el:
                separator = ('-' * 4 if 0 <= i < 10 else '-' * 3)  # Условие для 1 и 2 матрицы
                if 99 < i < 999:  # Условие для 3-й матрицы где после сложения появляются 3-х значные числа
                    separator = '-' * 2
                print(str(i), end=separator)
            print('')
        print(decor, '\n')

    def get_str_descriptive_output(self):
        """Функция обеспечивает аккуратный 'читабельный' вывод матрицы на экран используя строковое представление"""
        # Будет выведен на экран титул таблицы с матрицей, дальнейшая реализация вывода будет осуществлена
        # через перегрузку оператора __str__
        decor = '*****' * self.length
        print(f'\nПредставление матрицы # {Matrix._number_of_created_matrix}', decor, sep='\n')
        return str(self)

    @staticmethod
    def get_format_output(x):
        """ Аккуратный вывод полученных значений"""
        if 0 <= x < 10:
            x = str('00') + str(x)
        elif 10 <= x < 100:
            x = str('0') + str(x)
        else:
            x = str(x)
        return x


# 3. основной блок программы

matrix_1 = Matrix(10)
# matrix_1.get_int_descriptive_output()
matrix_1.get_str_descriptive_output()

matrix_2 = Matrix(10)
# matrix_2.get_int_descriptive_output()
matrix_2.get_str_descriptive_output()

matrix_sum = matrix_1 + matrix_2
# matrix_sum.get_int_descriptive_output()
matrix_sum.get_str_descriptive_output()

# На экран будут выведены две псевдорандомных матрицы и третья - представляющая результат сложения их элементов
# *!Синяя изолента! - есть вопросы к работе программы, нужно 'пофиксить' надосуге
# С учебной целью и для демонстрации хода реализации логики построения программы код был оставлен в таком виде.
