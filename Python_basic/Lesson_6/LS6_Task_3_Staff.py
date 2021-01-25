""" Author: Maksim Sapunov msdir6199@gmail.com 23/01/2021"""

# Задача 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position,
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных
# данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
    """ Общая модель сотрудника """
    _wage = 24300
    _bonus = 50000

    def __init__(self, name, surname, position):
        """ Конструктор класса Worker """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": self._wage, "bonus": self._bonus}


class Position(Worker):
    """ Дочерний класс описывающий позицию сотрудника"""

    def get_full_name(self):
        """ Выводит информацию о фамилии и имени сотрудника """
        return self.surname.title() + ' ' + self.name.title()

    def get_total_income(self):
        """ Выводит информацию о доходах сотрудника """
        report = 'Оклад сотрудника - ' + str(self._income['wage']) + \
                 '.\n Премия сотрудника - ' + str(self._income['bonus'])
        return report


a = Position('Олег', 'Петров', 'мастер')
print('\n\033[32mОтчет о сотруднике\n', '-'*30, '\n',
      a.get_full_name(), ' - ', a.position, '\n', a.get_total_income())
