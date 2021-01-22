"""Author - Maksim Sapunov, msdir6199@gmail.com 21/01/2021"""

# Задача 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

file_path = 'to_task_6.txt'  # Путь к файлу с данными

with open(file_path, 'r') as f:  # Открываем файл менеджером и сохраняем строки в список
	content = f.readlines()

study_dict = {}  # Создаем словарь в который будем сохранять результат

# Парсим строку в повторных циклах
for line in content:
	divide_line = line.split(':')
	len_dl = len(divide_line[1])
	integer = []
	i = 0
	while i < len_dl:
		st_digit = ''  # Здесь будем сохранять цифры
		a = divide_line[1][i]
		while '0' <= a <= '9':  # Условие для выбора цифр из символов строки
			st_digit += a
			i += 1
			if i < len_dl:
				a = divide_line[1][i]
			else:
				break
		i += 1
		if st_digit != '':
			integer.append(int(st_digit))  # Интуем строку и добавляем ее в конец списка
	sum_lesson = 0
	for value in integer:
		sum_lesson += value
	study_dict[divide_line[0]] = sum_lesson

print(study_dict)  # Распечатываем словарь.
