"""Author - Maksim Sapunov, msdir6199@gmail.com 21/01/2021"""

# Задача 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет строк и слов в каждой строке

def how_much_words(string: str):
    """Производит подсчет слов в строке"""
    return len(string.split())


work_file = 'to_task_2.txt'  # Указываем файл для считывания данных

with open(work_file, 'r') as f_obj:  # Содержимое файла сохраняем в переменную в виде списка
    content = f_obj.readlines()

print(f'Количество строк в указанном файле: {len(content)}')  # Распечатываем количество строк
line_number = 1  # Создаем счетчик строк
for line in content:  # В цикле с использованием функции проводим подсчет количества слов в строке
    print(f'В строке # {line_number } - {how_much_words(line)} слов.')
    line_number +=1
