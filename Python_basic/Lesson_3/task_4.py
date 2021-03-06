"""Author - Maksim Sapunov msdir6199@gmail.com 02/01/2021"""

# task_4 . Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    """
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: результат возведения x в степень y
    """
    # возведение x в отрицательную степень y = 1 / x в положительной степени y
    y = -y
    tmp = x
    # согласно условию задачи возводим x в степень y не используя встроенную функцию возведения в степень
    for i in range(1, y):
        tmp = tmp * x
    # выполняем финальное вычисление и возвращаем результат
    return 1/tmp


# основной блок программы
x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
# пропущен блок проверки правильности ввода данных пользователем
result = my_func(x, y)
print(f'Результат возведения {x} в степень {y} равен: {result}.')
