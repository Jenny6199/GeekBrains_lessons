"""Autor: Maksim Sapunov msdir6199@gmail.com"""

# Открываем файл для чтения
with open('text6.txt', 'r') as f:
	content = f.readlines()
# Cоздаем пустой словарь
my_dict = {}

# Парсим строку в повторных циклах
for line in content:
	divide_line = line.split(':')
	l = len(divide_line[1])
	integer = []
	i = 0
	while i < l:
		s_int = ''
		a = divide_line[1][i]
		while '0' <= a <= '9':
			s_int += a
			i += 1
			if i < l:
				a=divide_line[1][i]
			else:
				break
		i+=1
		if s_int != '':
			integer.append(int(s_int))
	sum_lesson = 0
	for value in integer:
		sum_lesson += value
	my_dict[divide_line[0]] = sum_lesson
# Распечатываем словарь
print(my_dict)
