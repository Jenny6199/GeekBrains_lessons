""" Author: Maksim Sapunov msdir6199@gmail.com 23/01/2021"""

# Задача 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color ()цвет  и метод running
# (запуск). Атрибут  реализовать как приватный. В рамках метода  реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния составляет 7 секунд, второго - 2 секунды, третьего - любое
# Переключение между режимами должно осуществляться только в указанном порядке.
# Проверить работу примера, создав экземпляр класса и вызвав указаный метод.

# Понимаю что обстоятельно, но пока короче не получается :(
import time

color_index = {
    1: '\033[31m',  # красный
    2: '\033[32m',  # желтый
    3: '\033[33m',  # зеленый
    0: '\033[0m'}   # очистить формат


class TrafficLight:
    """ Простое представление светофора """
    color = 1

    def running(self):
        """ Запуск светофора (задержка по умолчанию 7-2-7)"""
        for i in range(3):
            if self.color == 1:
                text = 'КРАСНЫЙ'
                delay = 7
            elif self.color == 2:
                text = 'ЖЕЛТЫЙ'
                delay = 2
            else:
                text = 'ЗЕЛЕНЫЙ'
                delay = 7

            print(f'{color_index[self.color]}{text}{color_index[0]}')
            time.sleep(delay)
            if self.color < 3:
                self.color += 1
            else:
                self.color = 1
        return


Crossroad_883 = TrafficLight()  # Создаем экземпляр светофора
Crossroad_883.running()  # Метод запуска светофора
