"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Реализовать два скрипта
# 1 - итераторб генерирующий целые числа, начиная с указанного

from sys import argv
from itertools import count, cycle
from random import randint


script_name, start = argv
list_ex = []
for el in count(int(start)):
    if el > 10:
        break
    else:
        list_ex.append(el)
print(list_ex)
