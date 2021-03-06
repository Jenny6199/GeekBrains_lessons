"""Author - Maksim Sapunov msdir6199@gmail.com 02/01/2021"""

# task_6 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘in_txt’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(string: str):
    """
    Функция принимает текст, и возвращает его с заглавной буквы
    :param string - текст (отдельное слово)
    :return string.title()
    """
    return string.title()


def text_func(in_txt: str):
    """
    Функция принимает текст, разбивает его на отдельные слова и возвращает все слова с заглавной буквы
    используя функцию int_func()
    :param in_txt - строка (слова разделенные пробелами)
    :return string - модифицированная строка содержащая все слова с заглавной буквы
    """
    tmp = list(in_txt.split(' '))
    string = ''
    for i in range(0, len(tmp)):
        tmp[i] = int_func(tmp[i])
        string += (tmp[i] + ' ')
    return string


# основное тело программы
text = input('Введите тест: ')
print(text_func(text))
