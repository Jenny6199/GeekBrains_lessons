"""Author - Maksim Sapunov, msdir6199@gmail.com 15/01/2021"""

# Задача #2: Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых будет больше
# предыдущего элемента. Элементы, удовлетворяющие условию, оформить в виде спискаю Для его формирования используйте
# генератор.


def generate_and_filtration(length: int):
    """
    Функция генерирует случайный список чисел заданной длины, после чего создает на его основе второй,
    список при условии что каждый последующий его элемент в родительском списке был больше предыдущего.
    Выводит оба списка на экран.
    :param length: целое число -  длина генерируемого списка
    :return: None
    """

    from random import random

    random_list = [random()*10 for el in range(length)]
    new_list = [random_list[el] for el in range(0, len(random_list)) if random_list[el] > random_list[el-1]]

    print("Cлучайный список: ")
    print("---------------------------------------")
    for value in random_list:
        print(value)
    print("Список фильтрованный по условию задачи: ")
    print("---------------------------------------")
    for value in new_list:
        print(value)


if __name__ == '__main__':
    generate_and_filtration(10)
