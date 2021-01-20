"""Author - Maksim Sapunov, msdir6199@gmail.com 02/01/2021"""

# task_1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#       Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(digit_1: int, digit_2: int):
    """
    :param digit_1: Целое число, делимое
    :param digit_2: Целое число, делитель
    :return: результат деления digit_1 / digit_2 (float)
    """

    if digit_2 == 0:
        print('Попытка деления на ноль! Расчет не выполнен')
        return None
    else:
        return digit_1/digit_2


if __name__ == '__main__':
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    c = division(a, b)
    print(f'Результат деления: {c}')
