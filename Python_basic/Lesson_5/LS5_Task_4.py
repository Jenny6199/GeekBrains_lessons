"""Author - Maksim Sapunov, msdir6199@gmail.com 21/01/2021"""

# Задача 4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк доллжен записываться в новый текстовый файл.


def change_digit_to_rus(number):
    """Преобразует числительные в русский текст"""
    numbers = {'1': 'Один',
               '2': 'Два',
               '3': 'Три',
               '4': 'Четыре',
               '5': 'Пять',
               '6': 'Шесть',
               '7': 'Семь',
               '8': 'Восемь',
               '9': 'Девять',
               '0': 'Ноль'}
    if str(number) in numbers:
        return numbers[str(number)]


def get_data(file_path: str):
    """
    Функция производит выгрузку данных из файла и возвращает их в виде переменной
    :param file_path: путь к файлу из которого производится выгрузка данных
    :return: список с числительными полученных из строк файла.
    """
    with open(file_path, 'r') as f_obj:
        digit_list = []
        for line in f_obj:
            data = line.split()
            number = data[2]
            digit_list.append(number)
    return digit_list


def save_data(file_path: str):
    """Функция сохраняет данные в указанный файл"""
    with open(file_path, 'w') as rf_obj:
        for value in get_data(data_file):
            string = change_digit_to_rus(value) + ' - ' + value + '\n'
            rf_obj.writelines(string)


data_file = 'to_task_4.txt'
result_file = 'from_task_4.txt'

print('Данная программа преобразует наименование английских числительных в русские и сохранит их в отдельный файл.')
save_data(result_file)
print('Программа завершила свою работу - исходный и конечный файл сохранены.')
