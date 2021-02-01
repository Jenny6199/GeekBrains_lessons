""" Author: Maksim Sapunov msdir6199@gmail.com 30/01/2021"""

# Задача 1. Реализовать класс «Дата».
# Функция-конструктор класса должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# Пример '08-08-1983'

import re  # Использована для отработки навыков использования регулярных выражений.


class Date:
    """ Реализует преобразование строкового представления о дате в числовое"""

    def __init__(self, text: str):
        """ Инициирует создание объекта класса
        :param text: str строка в которой будет осуществлен поиск
        """
        self.text = text
        self.date_text = str(re.findall(r'\d{2}-\d{2}-\d{4}', text))

    def get_date_info(self):  # Создана для удобства чтения и оформления кода.
        """Функция возвращает словарь с датами найденными в строке методом convert_date_to_digit"""
        return Date.convert_date_to_digit(self.date_text)

    @classmethod
    def convert_date_to_digit(cls, text: str):
        """Функция получает строковое представление даты и возвращает словарь содержащий в числовом представлении
        день, месяц, год """
        result = [el for el in re.split(r'\D', text, maxsplit=0) if el.isdigit()]
        digit_date = {
            'day': int(result[0]),
            'month': int(result[1]),
            'year': int(result[2])}
        return digit_date

    @staticmethod
    def get_descriptive_output(date_inf: dict):
        """ Функция обеспечивает валидацию полученных данных и аккуратный вывод даты на экран"""
        if date_inf['day'] < 31 and date_inf['month'] < 12 and date_inf['year'] != 0:
            print('В тексте были найдены следующие сведения о датах:', '\n',
                  f'День: {date_inf["day"]}, Месяц: {date_inf["month"]}, Год: {date_inf["year"]}')
        else:
            print('Получены значения не соответствующие дате.')


# Примеры текстовых объектов
bd = Date('День рождения у моего друга 08-08-1983')
sl = Date('26-05-2017 мы были на высоте 4672,1 метров')
wr = Date('Данное сообщение с ложными 82-14-9472 данными')
dv = Date('Первое погружение 21-08-2011 мы проводили на обогащенном воздухе')
examples = (bd, sl, wr, dv)

# Проверка работоспособности программы
for element in examples:
    print(f'Для анализа представлена строка: {element.text}')
    element.get_descriptive_output(element.get_date_info())
    print('-'*30)
