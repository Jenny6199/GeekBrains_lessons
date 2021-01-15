"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Задача #5: Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce

work_list = [el for el in range(100, 1001)]
multiply_all = reduce(lambda el_1, el_2: el_1 * el_2, work_list)
print(multiply_all)
