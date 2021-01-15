"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Задача #6: Реализовать два небольших скрипта...
# Подзадача #1 - итератор генерирующий целые числа, начиная с указанного (до 10)

from sys import argv
from itertools import count


script_name, start = argv
list_ex = []
for el in count(int(start)):
    if el > 10:
        break
    else:
        list_ex.append(el)
print(list_ex)
