""" Author: Maksim Sapunov msdir6199@gmail.com 25/01/2021"""


# Задача 5. Реализовать класс Stationary (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение "Запуск отрисовки.".
# Создать три дочерних класса Pen Pencil Handle. В каждом из классов реализовать переопределение draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:
    """ empty docstring"""

    title = 'Запуск отрисовки.'

    def draw(self):  # Первый вариант функции - родительский класс.
        """ Выводит титульное сообщение """
        print(f'{self.title} - для луших результатов '
              f'необходимо выбрать инструмент.\n')


class Pen(Stationary):  # Дочерний класс - имеет отличительный параметр - толщина пера
    """ Простое представление шариковой ручки """

    def __init__(self, thickness: int):
        self.thickness = thickness
        self.name = 'шариковая ручка'

    def draw(self):   # переопределние функции согласно условию задачи (выводит другое сообщение)
        """ Информирует о выбранном инструменте для выполнения рисунка """
        print(f'{self.title} - {self.name} - толщина пера #{self.thickness}.\n')


class Pencil(Stationary):  # Дочерний класс - имеет отличительный параметр жесткость карандаша
    """ Простое представление карандаша """

    def __init__(self, hardness: str):
        self.hardness = hardness
        self.name = 'простой карандаш'

    def draw(self):  # переопределние функции согласно условию задачи (выводит другое сообщение)
        """ Информирует о выбранном инструменте для выполнения рисунка """
        print(f'{self.title} - {self.name} - жесткость {self.hardness}')
        print(f'Не забывайте периодически точить {self.name} для лучших результатов.\n')


class Handle(Stationary):  # Дочерний класс - имеет отличительный параметр цвет
    """ empty docstring """

    def __init__(self, color: str):
        self.color = color
        self.name = 'перманентный маркер'

    def draw(self):  # переопределние функции согласно условию задачи (выводит другое сообщение)
        """ Информирует о выбранном инструменте для выполнения рисунка """
        print(f'{self.title} - {self.name} - цвет маркера  {self.color}')
        print(f'Осторожно! {self.name} нельзя стереть с рисунка!\n')


# Проверка работы метода draw в зависимости от выбранного объекта
general_s = Stationary()
general_s.draw()

pen = Pen(3)
pen.draw()

pencil = Pencil('HB')
pencil.draw()

marker = Handle('Red')
marker.draw()