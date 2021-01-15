"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Задача # 4: Представлен список чисел. Определите элемнты списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

# Решение:
from random import randint


def non_repeated_list(array: list):
    """
    Функция принимает список, формирует и возвращает список с элементами не повторяющимися в родительском списке.
    :param array: list
    :return: list - non_repeated elements of parents list
    """
    return [el for el in array if array.count(el) < 2]


# Тестовый список
list_ex = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Тестовый список 2
list_random = [randint(1, 100) for el in range(20)]

# Основной блок
if __name__ == '__main__':
    print(non_repeated_list(list_ex))
    print(non_repeated_list(list_random))
