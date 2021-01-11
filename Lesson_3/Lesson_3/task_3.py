"""Author - Maksim Sapunov msdir6199@gmail.com 02/01/2021"""

# task_3 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(digit_1, digit_2, digit_3):
    """
    функция принимает три числа и возвращает сумму наибольших двух из них
    :param digit_1 integer,
    :param digit_2 integer,
    :param digit_3 integer
    :return sum of two largest digit from this digits
    """

    digits = [digit_1, digit_2, digit_3]
    summa_max = 0
    # в цикле выбираем из списка полученных чисел максимальное заданное количество раз и суммируем
    for i in range(2):
        tmp = max(digits)
        summa_max += digits.pop(digits.index(tmp))
    print(summa_max)


my_func(3.25, 11.4, 12.8)
