"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Задача #6...  реализовать два небольших скрипта:
# Подзадача #2. Итераторб повторяющий элементы некоторого списка, определенного заранее

from random import randint
from itertools import cycle
from sys import argv

script_name, len_of_list = argv
# Случайное заполнение списка с помощью генератора
list_random = [randint(1, 100) for el in range(int(len_of_list))]
# Определение условия выхода из цикла
flag = 0
# Счетчик для визуального оформления вывода
divider = 0

for el in cycle(list_random):
    flag += 1
    if flag > 50:
        break
    else:
        if divider == len(list_random):
            print('\n--------------')
            divider = 0
        print(el, end=' ')
        divider += 1
