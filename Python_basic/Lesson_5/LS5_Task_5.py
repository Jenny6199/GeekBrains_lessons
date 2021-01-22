"""Author - Maksim Sapunov, msdir6199@gmail.com 21/01/2021"""

# Задача 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсичтывать сумму чисел в файле и выводить ее на экран.

from random import randint

list_of_numbers = [randint(0, 100) for el in range(10)]
print(f'В результате псевдослучайной генерации получен список:\n {list_of_numbers}')
file_path = 'to_task_5.txt'
print(f'Результат работы программы будет сохранен в файл: {file_path}')

try:
    f = open(file_path, 'w')
    string = ''
    summ = 0
    for i in list_of_numbers:
        string += str(i) + ' '
        summ += i
    print(f'Сгенерированный список: {string}\nСумма всех чисел в списке: {summ}', file=f, sep=' ')
    print(f'Cумма всех чисел в списке = {summ}')
    f.close()
except IOError:
    print('Ошибка ввода-вывода! Данные не сохранены.')

